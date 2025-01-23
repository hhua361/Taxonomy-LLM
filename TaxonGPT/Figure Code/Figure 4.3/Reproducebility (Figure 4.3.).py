import re
import pandas as pd


# Define the function to extract character information
def extract_characters(file_content):
    # Try multiple regex formats to ensure extraction ignores colons and other punctuation
    patterns = [
        re.compile(r'Character\s*\d+'),
        re.compile(r'Character\d+'),
        re.compile(r'Character\s*\d+\s*:'),
        re.compile(r'Character\d+\s*:'),
    ]

    characters = []
    for pattern in patterns:
        characters.extend(pattern.findall(file_content))

    # Remove extra colons and whitespace
    cleaned_characters = [re.sub(r'\s*:\s*', '', char).strip() for char in characters]

    # Keep all occurrences of character information, do not deduplicate
    return cleaned_characters


# Read the file content
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Check the extracted characters
def check_extracted_characters(file_paths, all_characters):
    for i, chars in enumerate(all_characters):
        print(f"Characters extracted from {file_paths[i]}:")
        for char in chars:
            print(char)
        print("\n")


# Remove duplicate characters and maintain order
def remove_duplicates(char_list):
    seen = set()
    unique_chars = []
    for char in char_list:
        if char not in seen:
            unique_chars.append(char)
            seen.add(char)
    return unique_chars


# Standardize the length of character lists
def normalize_characters(char_lists):
    max_length = max(len(chars) for chars in char_lists)
    normalized = []
    for chars in char_lists:
        normalized.append(chars + ['Character X: Placeholder'] * (max_length - len(chars)))
    return normalized


# Calculate the consistency ratio
def calculate_consistency(base_chars, other_chars):
    base_count = {char: base_chars.count(char) for char in set(base_chars)}
    other_count = {char: other_chars.count(char) for char in set(other_chars)}

    matches = sum(min(base_count.get(char, 0), other_count.get(char, 0)) for char in base_count)
    total = sum(base_count.values())
    return matches / total if total > 0 else 0

# dataset
# Dataset4 (17 species 28 character)
# Dataset5 (12 species 72 character)
# Dataset6 (12 species 11 character)
# Dataset7 (24 species 24 character)
# Dataset8 (13 species 29 character)
# Dataset9 (18 species 17 character)
# Dataset10 (14 species 75 character)
# Dataset11 (19 species 18 character)
# API
# Web


# List of file paths
file_paths = [
    "E:/Evaluate_results_for_all_datasets/Dataset11 (19 species 18 character)/API/1.txt",
    "E:/Evaluate_results_for_all_datasets/Dataset11 (19 species 18 character)/API/2.txt",
    "E:/Evaluate_results_for_all_datasets/Dataset11 (19 species 18 character)/API/3.txt",
    "E:/Evaluate_results_for_all_datasets/Dataset11 (19 species 18 character)/API/4.txt",
    "E:/Evaluate_results_for_all_datasets/Dataset11 (19 species 18 character)/API/5.txt"
]

# Extract character information from all files
all_characters = [extract_characters(read_file(file_path)) for file_path in file_paths]

# Remove duplicate characters and maintain order
all_characters = [remove_duplicates(chars) for chars in all_characters]

# Check the extracted characters
check_extracted_characters(file_paths, all_characters)

# Standardize the length of character lists
normalized_characters = normalize_characters(all_characters)

# Select the base result (the first file)
base_characters = normalized_characters[0]

# Compare other results with the base result
consistencies = [calculate_consistency(base_characters, chars) for chars in normalized_characters[1:]]

# Keep three decimal places
consistencies = [round(consistency, 3) for consistency in consistencies]

# Calculate the average consistency ratio and keep three decimal places
average_consistency = round(sum(consistencies) / len(consistencies), 3)

# Output results
print(f"Consistency ratios of each repetition: {consistencies}")
print(f"Average consistency ratio: {average_consistency:.3f}")

# Generate a DataFrame of consistency results
results_df = pd.DataFrame({
    'File': [f'Repeat {i + 1}' for i in range(1, len(file_paths))],
    'Consistency Ratio': consistencies
})

# Display results
print(results_df)
