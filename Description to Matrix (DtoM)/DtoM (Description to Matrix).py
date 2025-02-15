import json
from openai import OpenAI
import os
import re

# Initialize the OpenAI client with the API key
# Retrieve the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    # Raise an error if the API key is not found
    raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")

# Create an OpenAI client instance
client = OpenAI(api_key=api_key)

# Define the path to the file containing species descriptions
file_path = "species_descriptions.txt"

# Read the content of the file into the_original_description
try:
    with open(file_path, "r", encoding="utf-8") as file:
        the_original_description = file.read()
except FileNotFoundError:
    raise ValueError(f"File not found at the specified path: {file_path}")
except Exception as e:
    raise ValueError(f"An error occurred while reading the file: {e}")

# Debug: Print the loaded description to ensure it was read correctly
print("The original taxonomic description loaded successfully:")
print(the_original_description[:500])  # Print the first 500 characters for verification

# Messages to guide the generation of the character list
messages_character_list = [
    {"role": "system",
     "content": """
     You are a taxonomist specializing in morphological character analysis. 
     The following is a taxonomic description involving multiple species that share a phylogenetic relationship and belong to the same major group.
     Your task is to analyze the descriptions and extract morphological characteristics to generate a universal character list suitable for constructing a character matrix for phylogenetic analysis.
     """},
    {"role": "system",
     "content": """
     When generating the character list, please ensure the following:
     - **Taxonomic Standards**: The character list must conform to biological and taxonomic standards.
     - **Character Independence**: Each character should be independent, describing only one morphological attribute. Avoid combining multiple attributes into a single character.
     - **Character States**: For each character, list all possible states as observed in the descriptions. The states should be discrete and correspond to the relevant description content.
     - **Avoid Quantitative Characters**: Try to avoid selecting quantitative characters (e.g., measurements like length or size). Focus on qualitative characters that are more suitable for phylogenetic analysis.
     - **Shared Derived Characters**: Select characters that are informative for distinguishing among the species in the dataset, focusing on shared derived characters (synapomorphies).
     """},
    {"role": "system",
     "content": """
     Please present the character list in the following JSON format:
     ```json
     {
         "1": {
             "description": "Detailed description of Character 1",
             "states": {
                 "1": "Character 1, State 1",
                 "2": "Character 1, State 2"
             }
         },
         "2": {
             "description": "Detailed description of Character 2",
             "states": {
                 "1": "Character 2, State 1",
                 "2": "Character 2, State 2",
                 "3": "Character 2, State 3"
             }
         },
         ...
     }
     ```"""},
    {"role": "user",
     "content": f"""
     Please generate the character list as per the requirements above.
     Here is the combined taxonomic description of all species in the dataset:
     {the_original_description}
     """}
]

# Generate the initial character list using OpenAI API
try:
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=messages_character_list,
        stop=None,
        temperature=0,
        n=1
    )
except Exception as e:
    print(f"API call failed: {e}")
    exit()

# Capture the character list as string
character_list = response.choices[0].message.content


# Function to parse the character list string
def parse_character_list(character_list_str):
    """
    Parse the character list returned by the OpenAI API and clean up the string for JSON parsing.
    """
    # Debug: Print the raw character list before cleaning
    print("Raw character list before cleaning:\n", character_list_str)

    # Remove unwanted '```json' and '```' markers from the beginning and end
    cleaned_str = re.sub(r'```(?:json)?|```', '', character_list_str)  # Remove '```json' and trailing '```'

    # Clean leading/trailing whitespaces or newlines
    cleaned_str = cleaned_str.strip()

    # Debug: Print the cleaned character list for inspection
    print("Cleaned character list:\n", cleaned_str)

    try:
        # Parse the cleaned JSON string
        parsed_json = json.loads(cleaned_str)
        print("Parsed JSON successfully.")
        return parsed_json
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Failed JSON: {cleaned_str}")
        return None


# Parse the character list
character_dict = parse_character_list(character_list)

if character_dict:
    print("Parsed character list dictionary:\n", character_dict)
else:
    print("Error: Failed to parse the character list.")


# Extract corresponding character state from the description and format the output
def api_extract_state(description, character_info, character_id):
    messages_extract_information = [
        {"role": "system",
         "content": """
                 You are a taxonomy expert skilled in extracting morphological character information from taxonomic descriptions.
                 Based on the provided description and possible states, you will extract the specific state(s) for the given character. 
                 Additionally, if the description indicates more than one state for a character, list all relevant states (e.g., state1 and state2). 
                 If no information about the character is found in the description, mark the state as 'Missing (?)'.
                 """},
        {"role": "system",
         "content": f"""
                To extract character information, follow these steps:
                1. **Strictly ensure that the final generated matrix contains exactly the characters listed in the character list, in the specified order. You must strictly adhere to this character list, neither adding nor omitting any traits.**
                2. For each character, check if the species description includes any mention of the character's states. If it does, accurately record the corresponding state number.
                3. If the description does not mention any character states, use your language reasoning skills to strictly check for words indicating the absence of the characteristic (e.g., "non", "no", "not"). If such terms are present, use the corresponding state number based on your reasoning.
                4. If there is no mention of the character's states in the species description and your reasoning confirms the absence of relevant content, use "Gap" to represent this.
                5. For trait states that do not exist (called "Missing"), use the symbol "-".
                """},
        {"role": "system",
         "content": f"""
                After generating the extraction results in list format, please sort the traits and their corresponding states for each species **in the exact order they appear in the character list**, from left to right.
                In the example, the first '1' indicates that character 1 has state number 1 for the species.
                Arrange the list format results accurately as shown in the example.
                For content where a character may have multiple possible states, use (12) to indicate that the character has either state 1 or state 2.
                """},
        {"role": "system",
         "content": """
                Please output the result using the following format:
                character{character_id}: stateX (state description) 
                If the character has multiple states, output them as:
                character{character_id}: stateX (state description) and stateY (state description)
                If the character information is missing from the description, output: 
                character{character_id}: Missing (?)
                """},
         {"role": "user",
          "content": f"""
             Here is the character description and states to extract:
             Character description: {character_info["description"]}
             Possible states: {json.dumps(character_info["states"], indent=2)}
             Here is the corresponding taxonomic description:
             {description}
             """
          }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=messages_extract_information,
            stop=None,
            max_tokens=1000,
            temperature=0,
            n=1
        )
        # Retrieve and return the formatted character state information
        state_information = response.choices[0].message.content
        return state_information.strip()
    except Exception as e:
        print(f"API call failed: {e}")
        return None


# Function to iteratively extract each character and its state
def extract_character_for_species(character_dict, species_description):
    """
    Extract character states for a given species description based on the parsed character list.

    Args:
        character_dict (dict): A dictionary containing character IDs as keys and their information
                               (description and states) as values.
        species_description (str): The description of the species from which character states will be extracted.

    Returns:
        dict: A dictionary mapping character IDs to their extracted states.
    """
    # Dictionary to store the extracted character states for the species
    species_character_states = {}

    # Iterate over each character in the character dictionary
    for character_id, character_info in character_dict.items():
        # Prepare a dictionary containing the description and states of the current character
        character_full_info = {
            "description": character_info["description"],
            "states": character_info["states"]
        }

        # Use the API to extract the state(s) for the character from the species description
        state = api_extract_state(species_description, character_full_info, character_id)

        # If a state is extracted (non-empty), add it to the result dictionary
        if state:
            species_character_states[character_id] = state

    return species_character_states


# Parse the matrix information to the dictionary format
def parse_to_matrix(character_dict):
    """
    Parses the extracted result in dictionary format and converts it into a matrix format.
    Adds exception handling to ensure robustness.
    """
    # Initialize an empty matrix row to represent the character states for the species
    matrix_row = []

    # Iterate through the dictionary of extracted results
    for character_id, character_state in character_dict.items():
        # Handle potential None or non-string values
        if not isinstance(character_state, str):
            matrix_row.append('-')  # If character_state is invalid, mark it as missing
            continue

        # Prioritize matching 'stateX' and extract X
        states = re.findall(r'state(\d)', character_state)  # Extract the number following 'stateX'

        # If no 'stateX' is found, attempt to match other valid individual state numbers
        if not states:
            states = re.findall(r'(?<![A-Z])\b\d\b(?![A-Z])', character_state)  # Match other state numbers, excluding those surrounded by letters

        # If multiple states are found, sort them and add parentheses
        if len(states) > 1:
            sorted_states = sorted(map(int, states))  # Sort the numbers
            combined_state = f"({' '.join(map(str, sorted_states))})"
            matrix_row.append(combined_state)
        elif len(states) == 1:
            # If there is only one state, do not add parentheses
            matrix_row.append(states[0])
        else:
            # If no state is found, mark as missing with '-'
            matrix_row.append('-')

    # Format the matrix row into a string similar to "species: 1 (12) 1 1"
    matrix_str = " ".join(matrix_row)

    return matrix_str


# Parse the matrix information
def parse_matrix(matrix):
    """
    Parse the matrix string into a list of individual elements or groups of elements.
    Groups are identified by parentheses, while other elements are separated by spaces.
    """
    matrix = re.findall(r'\([^\)]+\)|\S+', matrix)  # Match groups in parentheses or standalone elements
    return matrix


# Verify the matrix is accurate based on the ChatGPT-4o API model
def validate_matrix(description, matrix, character_list, repetitions=3):
    """
    Call the API to verify the matrix multiple times and compare the results of multiple verifications.
    :param description: taxonomic description of the species
    :param matrix: feature matrix to be verified
    :param character_list: feature list
    :param repetitions: number of verification repetitions (default 3 times)
    :return: verification results and consistency report
    """
    messages = [
        {"role": "system", "content": """
            You are an expert in taxonomy and phylogenetic analysis.
            Your task is to validate the provided character matrix based on the given morphological 
            description and character list. Please follow these instructions:
            1. **Check each character in the matrix individually**:
                - Compare the state in the matrix with the content in the description.
                - Check if the state in the matrix matches any valid state in the character list.
            2. **If a discrepancy is found**:
                - Mark the result as **Error**.
                - Provide both the matrix state and the expected state from the description.
                - Suggest corrections if applicable.
            3. **If the state matches**, mark it as **Correct**.
            4. **If a character state is missing**, mark it as **Missing**, and suggest the expected state if possible.
            5. **If a character state is Not Applicable**, mark it as **Not Applicable**
            6. **For the Expexted state you should show the number in the [State from Description]
            5. **Output Format**:
                ```
                Species: [Species Name]
                Character Validation Report:
                - Character [ID]: [Character Description]
                  Matrix State: [State in Matrix]
                  Expected State: [ from DescriptionState]
                  Result: [Correct/Error/Missing/Not Applicable]
                ```
        """},
        {"role": "user", "content": f"""
            Description: {description}
            Character List: {json.dumps(character_list, indent=2)}
            Matrix: {matrix}
        """}
    ]
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=messages,
        temperature=0,
        max_tokens=1000,
    )

    return response.choices[0].message.content


# Parse the API response to extract species name and character validation reports
def parse_api_response(api_response: str):
    """
    Parse the API response to extract species name and character validation reports.

    Args:
        api_response (str): The raw response string from the API.

    Returns:
        dict: A dictionary containing the species name and a list of character validation reports.
    """
    # Clean the response by removing surrounding code markers and whitespace
    api_response = api_response.strip("```").strip()

    # Initialize variables to store species name and character reports
    species_name = None
    character_reports = []
    current_report = {}

    # Split the response into lines for processing
    lines = api_response.split('\n')

    # Iterate through each line to extract relevant information
    for line in lines:
        line = line.strip()

        # Extract the species name
        if line.startswith("Species:"):
            species_name = line.split(":", 1)[1].strip()

        # Handle character validation report blocks
        elif re.match(r"^- Character \d+:", line):
            # Save the current report if it exists and start a new one
            if current_report:
                character_reports.append(current_report)
                current_report = {}

            # Extract character ID and description
            match = re.match(r"^- Character (\d+): (.+)", line)
            if match:
                current_report["Character ID"] = int(match.group(1))
                current_report["Character Description"] = match.group(2).strip()

        # Extract matrix state
        elif line.startswith("Matrix State:"):
            current_report["Matrix State"] = line.split(":", 1)[1].strip()

        # Extract expected state
        elif line.startswith("Expected State:"):
            current_report["Expected State"] = line.split(":", 1)[1].strip()

        # Extract validation result
        elif line.startswith("Result:"):
            current_report["Result"] = line.split(":", 1)[1].strip()

        # Extract suggestions for corrections
        elif line.startswith("Suggestion:"):
            current_report["Suggestion"] = line.split(":", 1)[1].strip()

    # Append the last report if it exists
    if current_report:
        character_reports.append(current_report)

    # Return the parsed results as a dictionary
    return {
        "Species": species_name,
        "Character Validation Report": character_reports,
    }


# Extract the numeric state from an expected state string
def extract_state(expected_state):
    """
    Extract the numeric state from an expected state string.

    Args:
        expected_state (str): The expected state string, possibly containing a number.

    Returns:
        str: The extracted numeric state, or the original state if no number is found.
    """
    # Search for a numeric value in the expected state string
    match = re.search(r'\d+', expected_state.strip())
    return match.group(0) if match else expected_state


# Update the matrix with the expected state for a specific character ID
def update_matrix(matrix, character_id, expected_state):
    """
    Update the matrix with the expected state for a specific character ID.

    Args:
        matrix (list): The matrix to be updated, represented as a list of elements.
        character_id (int): The ID of the character to update in the matrix.
        expected_state (str): The expected state to assign to the character.

    Returns:
        list: The updated matrix with the corrected state for the specified character ID.
    """
    current_index = 0  # Track the current character index in the matrix

    # Iterate through the matrix elements
    for i, char in enumerate(matrix):
        # Increment the index for each element, including grouped elements in parentheses
        current_index += 1

        # Update the matrix if the current index matches the character ID
        if current_index == character_id:
            matrix[i] = expected_state
            break

    return matrix


# Validate and correct the matrix based on API validation results
def validate_and_correct_matrix(matrix, api_results):
    """
    Validate and correct the matrix based on API validation results.

    Args:
        matrix (list): The matrix to validate and correct.
        api_results (dict): The API results containing validation reports.

    Returns:
        list: The corrected matrix after applying necessary updates.
    """
    # Process each validation report from the API results
    for report in api_results["Character Validation Report"]:
        if report["Result"] == "Error":  # Check if there is an error in the validation
            character_id = report["Character ID"]  # Extract the character ID
            expected_states = report["Expected State"].split(" or ")  # Split expected states
            expected_state = extract_state(expected_states[0])  # Use the first expected state

            # Update the matrix with the corrected state
            matrix = update_matrix(matrix, character_id, expected_state)

    return matrix


# Iteratively validates and updates a feature matrix, ensuring all errors are resolved with additional checks for robustness before finalizing the result
def validate_matrix_with_iterations(description, matrix, character_list, max_iterations=10):
    """
    Loop through the validation matrix and update when errors are found until there are no errors in the validation results.
    After the initial validation is error-free, perform two additional API validations to ensure that there are no errors before outputting the final results.
    :param description: taxonomic description of the species
    :param matrix: current feature matrix
    :param character_list: feature list
    :param max_iterations: maximum number of loops (to prevent infinite loops)
    :return: final validation results and matrix
    """
    iteration = 0
    while iteration < max_iterations:
        print(f"Iteration {iteration + 1}: Validating matrix...")

        validation_result = validate_matrix(description, matrix, character_list)
        parsed_result = parse_api_response(validation_result)

        errors_exist = any(
            report["Result"] == "Error" for report in parsed_result["Character Validation Report"]
        )

        if errors_exist:
            print("Errors found. Updating matrix...")
            matrix_list = parse_matrix(matrix)
            matrix = validate_and_correct_matrix(matrix_list, parsed_result)
            matrix = ' '.join(matrix)  # Converted to string format for API re-checking
        else:
            print("No errors found. Performing additional checks...")
            all_checks_passed = True  # Mark all additional checks as passed

            for i in range(2):
                print(f"Additional check {i + 1}...")
                additional_result = validate_matrix(description, matrix, character_list)
                additional_parsed = parse_api_response(additional_result)

                additional_errors_exist = any(
                    report["Result"] == "Error" for report in additional_parsed["Character Validation Report"]
                )

                if additional_errors_exist:
                    print("Error found during additional check. Repeating main loop...")
                    all_checks_passed = False  # If an error is found, mark it as not passed
                    break  # Jump out of the extra check and re-enter the main loop

            if all_checks_passed:
                print("Final validation passed with no errors.")
                return matrix

        iteration += 1  # Increase the iteration count

    print("Maximum iterations reached. Returning the latest matrix.")
    return matrix


# Generate a character matrix for a single species description, validate it, and apply updates
def process_single_species(description, character_dict):
    """
    Generate a character matrix for a single species description, validate it, and apply updates.

    Args:
        description (str): The description of the species.
        character_dict (dict): A dictionary containing the list of characters and their details.

    Returns:
        list: The final validated and updated matrix for the species.
    """
    # Extract character states from the species description
    species_character_states = extract_character_for_species(character_dict, description)

    # Convert the extracted character states into a matrix format
    species_matrix = parse_to_matrix(species_character_states)

    # Validate the matrix and apply updates iteratively
    final_matrix = validate_matrix_with_iterations(description, species_matrix, character_dict)

    return final_matrix


# Define a regular expression pattern to match species descriptions starting with a number
pattern = r"\n\d+ [A-Z][a-z]+ [A-Z][a-z]+"

# Split the original text into parts using the pattern
split_descriptions = re.split(pattern, the_original_description)

# Extract species names and their corresponding descriptions
species_matches = re.findall(pattern, the_original_description)
descriptions = []

for i, match in enumerate(species_matches):
    # Clean up the matched species name
    species_name = match.strip()

    # Retrieve and clean the corresponding description
    description = split_descriptions[i + 1].strip()

    # Combine the species name with its description
    descriptions.append(f"{species_name}\n{description}")

# Output the results
for i, description in enumerate(descriptions):
    print(f"Description {i + 1}:\n{description}\n")

# Print the final list of descriptions for further use
print(descriptions)


# List to store matrices for all species
all_species_matrices = []

# Iterate through each species description
for i, description in enumerate(descriptions):
    print(f"\nProcessing species {i + 1}...")

    # Process the description to generate the final matrix
    final_matrix = process_single_species(description, character_dict)

    # Append the resulting matrix to the list
    all_species_matrices.append(final_matrix)
    print(f"Species {i + 1} Matrix: {final_matrix}")

# Print all matrices after processing all species
print("\nAll Species Matrices:")
for i, matrix in enumerate(all_species_matrices):
    print(f"Species {i + 1} Matrix: {matrix}")

# Print the final matrix and the full list of matrices for reference
print("Final Matrix:", final_matrix)
print(all_species_matrices)


def generate_nexus_with_labels(all_species_matrices, character_dict):
    """
    Convert species character matrices and character list into a NEXUS format string
    with CHARLABELS and STATELABELS for phylogenetic analysis.

    Args:
        all_species_matrices (list): A list of character matrices for each species.
        character_dict (dict): A dictionary containing character information.

    Returns:
        str: The generated NEXUS format string.
    """
    # Number of species and characters
    n_tax = len(all_species_matrices)
    n_char = len(all_species_matrices[0].split())  # Assume all matrices have the same number of characters

    # Initialize the NEXUS string
    nexus_str = f"""#NEXUS
BEGIN DATA;
DIMENSIONS NTAX={n_tax} NCHAR={n_char};

[! This is an automatically generated NEXUS matrix for phylogenetic analysis.]
FORMAT MISSING=? GAP=- SYMBOLS="1234";

CHARLABELS
    """

    # Add character labels
    for char_id, char_info in character_dict.items():
        nexus_str += f"[{char_id}] '{char_info['description']}'\n"

    nexus_str += ";\n\nSTATELABELS\n"

    # Add state labels
    for char_id, char_info in character_dict.items():
        state_labels = ' '.join(f"'{state}'" for state in char_info["states"].values())
        nexus_str += f"{char_id} {state_labels},\n"

    # Remove the trailing comma and add the MATRIX block
    nexus_str = nexus_str.rstrip(",\n") + ";\n\nMATRIX\n"

    # Add species names and their corresponding matrices
    for i, matrix in enumerate(all_species_matrices):
        species_name = f"Species {i + 1}"
        nexus_str += f"'{species_name}' {matrix}\n"

    nexus_str += ";\nEND;\n"

    return nexus_str


# Generate the NEXUS content
nexus_content = generate_nexus_with_labels(all_species_matrices, character_dict)
print(nexus_content)

# Write the NEXUS content to a file
with open("phylogenetic_matrix_with_labels.nex", "w") as f:
    f.write(nexus_content)
