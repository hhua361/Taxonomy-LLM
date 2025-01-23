import json  # JSON handling library
from openai import OpenAI  # OpenAI client for API interactions
import os  # OS module for environment variable access
import random  # Random module for generating random values
import re  # Regular expressions module for pattern matching

# Initialize the OpenAI client using the API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Generate a random character list and store the result
number_about_the_character = 10  # Define the number of characters to be generated
num_species = 5  # Define the number of species to generate


# Messages to guide the generation of the character list
messages_character_list = [
    {"role": "system",
     "content":
         """You are now an expert in taxonomic research.
         Utilizing your knowledge in taxonomy, your task is to randomly generate a character list for a specific group of organisms.
         The character list should include the following:
         1. Character Descriptions: Provide detailed descriptions for each character.
         2. State Descriptions: Generate descriptions for the various states associated with each character.
         3. Taxonomic Principles: Ensure that the relationships between characters and their states are consistent with taxonomic principles, and the character and state description need to follow taxonomic principles.
         Please ensure that the character list is specific to a single taxonomic group. The final output should be presented in the following format:
         """},
    {"role": "system",
     "content": """Please make the result follow these formats:
            Species name:
            Character list format:
            {
            "1": {
                "description": "Detailed description of Character1",
                "states": {
                    "1": "Character1, State1",
                    "2": "Character1, State2"
                }
            },
            "2": {
                "description": "Detailed description of Character2",
                "states": {
                    "1": "Character2, State1",
                    "2": "Character2, State2",
                    "3": "Character2, State3"
                }
            },
            ...
            }
     """},
    {"role": "user",
     "content": f"""Please randomly generate a character list and indicate the relevant species name, and strictly follow the above requirements.
     When generating the character list, please ensure that the list contains exactly {number_about_the_character} characters 
    """}
]

# Generate the initial character list using OpenAI API
response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=messages_character_list,
    stop=None,
    max_tokens=1000,
    temperature=0,
    n=1
)

# Extract the generated character list from the API response
character_list = response.choices[0].message.content

# Output the character list
print(character_list)


# Parse and process the character list into a dictionary format
def parse_character_list(character_list_str):
    """
    Parse the character list string into a dictionary format.

    Args:
        character_list_str (str): The character list in string format.

    Returns:
        list: A list of state ranges for each character.
    """
    # Locate the JSON portion within the character list string
    json_start_index = character_list_str.find("```json")  # Find the start marker for the JSON block
    json_end_index = character_list_str.rfind("```")  # Find the end marker for the JSON block

    # Raise an error if the JSON block is not found
    if json_start_index == -1 or json_end_index == -1:
        raise ValueError("Could not find JSON format in the character list string.")

    # Extract the JSON string and strip any surrounding whitespace or markers
    json_str = character_list_str[json_start_index + len("```json"):json_end_index].strip()

    try:
        # Parse the JSON string into a Python dictionary
        character_dict = json.loads(json_str)
    except json.JSONDecodeError as e:
        # Raise an error with specific details if JSON parsing fails
        raise ValueError(f"JSON Decode Error: {e}")

    state_ranges = []  # Initialize a list to store state ranges for each character

    # Iterate through each character in the parsed dictionary
    for character in character_dict.values():
        # Extract the keys of the "states" dictionary and convert them to integers
        states = list(character['states'].keys())
        state_ranges.append([int(state) for state in states])

    return state_ranges  # Return the list of state ranges


# Randomly generate the matrix
def generate_random_matrix(num_species, state_ranges):
    """
    Generate a random matrix of character states for a given number of species.

    Args:
        num_species (int): The number of species to generate.
        state_ranges (list): A list of state ranges for each character.

    Returns:
        list: A matrix of randomly generated character states for each species.
    """
    matrix = []  # Initialize the matrix to store species data

    for i in range(num_species):
        species_name = f"SPECIES {i + 1}"  # Generate species name
        states = []  # Initialize the list of states for the species

        # Iterate over each character's state range
        for states_for_character in state_ranges:
            rand_choice = random.random()  # Generate a random number for state selection

            if rand_choice < 0.1:  # 10% chance of a missing state
                state = '-'
            elif rand_choice < 0.3:  # 20% chance of multiple states
                # Select multiple random states
                state_combination = random.sample(states_for_character, k=random.randint(2, len(states_for_character)))
                state_combination.sort()  # Ensure states are in ascending order
                state = f"({''.join(map(str, state_combination))})"
            else:  # 70% chance of a single state
                state = str(random.choice(states_for_character))

            states.append(state)  # Append the state to the states list

        # Add the species name and states to the matrix
        matrix.append([species_name] + states)

    return matrix  # Return the completed matrix


def print_matrix(matrix):
    """
    Print the matrix in a readable tabular format.

    Args:
        matrix (list): The matrix to be printed.
    """
    for row in matrix:
        print("\t".join(row))  # Print each row with tab-separated values


# Parse the character list into state ranges
state_ranges = parse_character_list(character_list)
print(state_ranges)

# Generate the random matrix
matrix = generate_random_matrix(num_species, state_ranges)
print(matrix)
print_matrix(matrix)


# Generate the description based on the character list and matrix information
def convert_matrix_to_knowledge_graph(matrix):
    """
    Convert a species matrix into a knowledge graph format.

    Args:
        matrix (list): A matrix containing species name and character states.

    Returns:
        dict: A dictionary representing the knowledge graph of the species.
    """
    species_name = matrix[0]  # Extract the species name (first element of the row)
    characteristics = {}  # Initialize a dictionary to store character states

    # Iterate through the character states in the matrix
    for i, state in enumerate(matrix[1:], start=1):  # Start index from 1 for Character1, Character2, etc.
        if state == '-':  # Handle missing state
            characteristics[f"Character{i}"] = "Missing"
        elif state.startswith('(') and state.endswith(')'):  # Handle multiple states
            states = state[1:-1]  # Remove parentheses
            state_desc = " or ".join([f"state {s}" for s in states])  # Format as "state X or state Y"
            characteristics[f"Character{i}"] = state_desc
        else:  # Handle single state
            characteristics[f"Character{i}"] = f"state {state}"

    # Return a dictionary representing the knowledge graph
    return {
        species_name: {
            "Characteristics": characteristics
        }
    }


def call_api_for_description(knowledge_graph, character_list):
    """
    Generate taxonomic descriptions using OpenAI API based on the knowledge graph and character list.

    Args:
        knowledge_graph (dict): The knowledge graph of a species.
        character_list (str): The character list in string format.

    Returns:
        str: The generated taxonomic description.
    """
    messages = [
        {"role": "system", "content": """
            You are a taxonomic assistant.
            **Task:**
            - Generate accurate and complete taxonomic descriptions for each species by mapping character state information to species morphological matrices.
            **Specific Requirements:**
            1. **Description Language:** Write standard academic taxonomic descriptions in English.
            2. **Content Inclusion:** The descriptions need to include all characters from the morphological matrix and accurately correspond to each character's state.
            3. **Description Format:**
                - **List Form:** List each character's state description according to its number.
                - **Paragraph Form:** Describe all character states in a paragraph, indicating the character numbers at appropriate places.
            4. **Handling Multiple States:** For characters with multiple states (e.g., "1 and 2"), accurately reflect that the taxon possesses all these states. For example: "Character 5: possesses both wings and antennae."
            5. **Avoid Subjective Information:** Strictly generate descriptions based on the provided data without including any errors or assumed information. Avoid subjective judgments.
            6. **Terminology Consistency:** Use consistent professional terminology to ensure the descriptions are professional and consistent.
            7. **Separate Presentation:** The taxonomic descriptions for each taxon should be presented separately to avoid any loss of information or confusion due to space constraints.
            8. **Data Format:**
                - **Morphological Matrix (knowledge_graph):** Provided in JSON format, structured as follows:
                ```json
                {
                    "taxon1": {
                        "character1": "state1",
                        "character2": ["state1", "state2"],  // Multiple states
                        ...
                    },
                    ...
                }
                ```
                - **Character Information (character_list):** Provided in JSON format, structured as follows:
                ```json
                {
                    "character1": {
                        "description": "Description of character 1",
                        "states": {
                            "state1": "Description of state 1",
                            "state2": "Description of state 2",
                            ...
                        }
                    },
                    ...
                }
                ```
            9. **Example:**
            **List Form:**
            - **Character 1:** State description.
            - **Character 2:** State description.
            - ...
            **Paragraph Form:**
            "1. State description. 2. State description. ..."
            **Note:** Include character numbers in the paragraph form.
        """},
        {"role": "user", "content": f"""
            Please generate standard taxonomic descriptions for all taxa based on the provided morphological matrix and character information.
            **Morphological Matrix (knowledge_graph):**
            {knowledge_graph}
            **Character Information (character_list):**
            {character_list}
            **Note:**
            - For characters with multiple states, please accurately reflect that the taxon possesses all these states.
            - Please strictly generate descriptions based on the provided data, avoiding any additional details or explanations that are not provided.
            - Each taxon's description should be presented separately.

        """},
        {"role": "assistant", "content": """
            Understood. I will strictly generate standard academic taxonomic descriptions for each taxon according to the provided morphological matrix and character state information.

            I will provide each taxon's description in both list form and paragraph form, indicating character numbers in the paragraph form, and accurately reflecting multiple states.
        """}
    ]

    response = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=messages,
            stop=None,
            temperature=0,
            n=1
        )

    description_content = response.choices[0].message.content

    return description_content


# Global variable to store species descriptions
species_descriptions_dict = {}


def process_species(matrix, character_list):
    """
    Process each species matrix to generate taxonomic descriptions.

    Args:
        matrix (list): A matrix containing species names and character states.
        character_list (str): The character list in string format.

    Returns:
        dict: A dictionary with species names as keys and their corresponding descriptions as values.
    """
    global species_descriptions_dict  # Global dictionary to store species descriptions
    species_descriptions = {}  # Initialize a local dictionary for the current processing

    # Iterate through each species matrix
    for species_matrix in matrix:
        # Convert the species matrix to knowledge graph
        knowledge_graph = convert_matrix_to_knowledge_graph(species_matrix)
        print(knowledge_graph)
        # Call the API to generate a taxonomic description
        description = call_api_for_description(knowledge_graph, character_list)
        # Extract the species name from the matrix
        species_name = species_matrix[0]
        # Store the generated description in the dictionary
        species_descriptions[species_name] = description

    # Update the global dictionary with the current species descriptions
    species_descriptions_dict.update(species_descriptions)

    return species_descriptions  # Return the descriptions for further use


# Generate species descriptions using the given matrix and character list
species_descriptions = process_species(matrix, character_list)

# Print each species description in a readable format
for species_name, description in species_descriptions_dict.items():
    print(f"Description for {species_name}:\n{description}\n")


def extract_matrix_from_description(species_name, description, character_list):
    """
    Extract the matrix information from a taxonomic description using OpenAI API.

    Args:
        species_name (str): The name of the species.
        description (str): The taxonomic description of the species.
        character_list (str): The character list in string format.

    Returns:
        str: The extracted matrix information.
    """
    messages_extract_information = [
        {"role": "system",
         "content": """
             You are an expert in taxonomic information extraction, skilled in extracting morphological character information from standard taxonomic descriptions based on a given character list.
             The character list specifies different characters and their states for all species in the dataset.
             Please generate a list-form extraction result for each species, listing the state of each trait.
             """},
        {"role": "system",
         "content": """
            To extract character information, follow these steps:
            First, check if the species description includes any mention of the character's states. If it does, correctly record the corresponding state label.
            If the description does not mention any character states, use your language reasoning skills to strictly check for words indicating the absence of the characteristic (e.g., "non," "no," "not"). If such terms are present, use the corresponding state label based on your reasoning.
            If there is no mention of the character's states in the species description and your reasoning confirms the absence of relevant content, use "Gap" to represent this.

            In the given character list, each character and state has a corresponding number.
            Please indicate the number for each trait's state in the generated list for each species.
            If a trait state does not exist, which will called "Missing" it symbol as '-'.
            """},
        {"role": "system",
         "content": """
            After generating the extraction results in list format, please sort the traits and their corresponding states for each species in ascending order, from left to right.
            In the example, the first '1' indicates that character 1 has state number 1 for the species.
            Arrange the list format results accurately as shown in the example.
            For content with multiple feature states use (12) to indicate that the CHARACTER has both states of serial number 1, 2.
            """},
        {"role": "system",
         "content": """
             Please make the result follow these formats,and don't need to show any other things, please only show the below results:
             Matrix information:
             SPECIES NAME : 1 2 1 3 3 (12) 2 (13)
             """},
        {"role": "user",
         "content": f"""
         Here is the character list {character_list} 
         Here is the corresponding taxonomic description for{species_name}:{description}"
         """},

    ]
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=messages_extract_information,
        stop=None,
        max_tokens=1000,
        temperature=0,
        n=1
    )

    matrix_information = response.choices[0].message.content

    return matrix_information


# Dictionary to store extracted matrices for each species
matrix_results = {}

# Loop through each species and its corresponding description
for species_name, description in species_descriptions_dict.items():
    # Extract matrix information from the species description
    matrix_info = extract_matrix_from_description(species_name, description, character_list)

    # Store the extracted matrix information in the results dictionary
    matrix_results[species_name] = matrix_info

# Print or process the extracted matrix information
for species_name, matrix_info in matrix_results.items():
    print(f"Matrix for {species_name}:\n{matrix_info}\n")

# Optionally print the entire dictionary of matrices
print(matrix_results)


def parse_matrix_to_knowledge_graph(matrix_dict):
    """
    Convert a taxonomic matrix dictionary into a structured knowledge graph JSON format.

    Args:
        matrix_dict (dict): The input matrix dictionary, e.g.,
            {
                'SPECIES 1': '\nLepidoptera mystica : 3 (123) 2 2 2 2 1 1 - 1 1 3 2 (123) 1 1',
                'SPECIES 2': '\nMatrix information:\nLepidoptera mystica : 2 2 3 2 (123) (12) (23) 2 3 3 (123) 2 2 2 1'
            }

    Returns:
        dict: The parsed knowledge graph in JSON format.
    """
    # Initialize the result dictionary to store the knowledge graph
    knowledge_graph = {}

    # Iterate through each species and its corresponding matrix
    for species, matrix in matrix_dict.items():
        # Remove prefixes and clean the matrix content
        matrix = re.sub(r".*?:", "", matrix).strip()

        # Split the matrix string into individual states
        states = matrix.split()

        # Initialize a dictionary to store characteristics for the species
        characteristics = {}

        # Iterate through each state and parse it
        for idx, state in enumerate(states, start=1):
            if state == "-":
                # Handle missing values
                parsed_state = "Missing"
            elif re.match(r"\(.*?\)", state):
                # Parse states enclosed in parentheses as alternative states
                parsed_state = " or ".join([f"state {s}" for s in state.strip("()").split("/")])
            else:
                # Parse single-state values
                parsed_state = f"state {state}"

            # Add the parsed state to the characteristics dictionary
            characteristics[f"Character{idx}"] = parsed_state

        # Update the knowledge graph with the species and its characteristics
        knowledge_graph[species] = {"Characteristics": characteristics}

    return knowledge_graph


def process_species2(matrix_dict, character_list):
    """
    Process each species matrix to generate taxonomic descriptions.

    Args:
        matrix_dict (dict): A dictionary containing species names and their character states.
        character_list (str): The character list in string format.

    Returns:
        dict: A dictionary with species names as keys and their corresponding descriptions as values.
    """
    # Initialize a global dictionary to store species descriptions
    global species_descriptions_dict_2
    species_descriptions_dict_2 = {}

    # Step 1: Convert the matrix dictionary to structured knowledge graph
    knowledge_graph = parse_matrix_to_knowledge_graph(matrix_dict)

    # Step 2: Generate taxonomic descriptions for each species
    for species_name, species_data in knowledge_graph.items():
        # Call an API to generate a taxonomic description based on species data
        description = call_api_for_description(species_data, character_list)

        # Store the generated description in the global dictionary
        species_descriptions_dict_2[species_name] = description

    # Return the global dictionary for further use
    return species_descriptions_dict_2


# Generate species descriptions using the given matrix and character list
species_descriptions2 = process_species2(matrix_results, character_list)

# Display each species description in a readable format
for species_name, description in species_descriptions_dict_2.items():
    print(f"Description for {species_name}:\n{description}\n")


def compare_description(description, desc, character_list):
    """
    Compare two taxonomic descriptions and identify differences in character states.

    Args:
        description (str): The original taxonomic description (description 1).
        desc (str): Another taxonomic description of the same species (description 2).
        character_list (str): The character list in string format to guide the comparison.

    Returns:
        str: A formatted string highlighting the differences between the two descriptions.
    """
    # Define the input messages for the OpenAI API
    messages = [
        {"role": "system", "content": """
            You are a taxonomic expert specializing in comparing taxonomic descriptions to identify differences between them. 
            I will provide you with two taxonomic descriptions of the same species.

            Both descriptions will involve morphological characters from the provided character list. 
            Your task is to compare the two descriptions and identify any differences in the character states for each character mentioned in the list.
            **Please only display the characters where there is a difference between the two descriptions.**
            """},
        {"role": "user", "content": """
            Please display the differences in the following format:

            - **Character Name**:
              - Description 1: [state in description 1]
              - Description 2: [state in description 2]
            """},
        {"role": "user", "content": f"""
            Here is description 1: {description}, which is the original taxonomic description.
            Here is description 2: {desc}, another taxonomic description of the same species.
            I will also provide you with a character list relevant to both descriptions. 
            Your task is to compare the two descriptions and, according to the instructions above, identify any differences between the two descriptions regarding the characters in the provided character list.
            {character_list}
            Please follow the specified format to display the differences.
            """}
    ]

    # Call the OpenAI API to compare the descriptions
    response = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=messages,
            stop=None,
            temperature=0,
            n=1
        )

    # Extract and return the comparison result from the response
    description_content = response.choices[0].message.content
    return description_content


# Compare the contents of the descriptions generated by the two methods
def compare_descriptions_between_dicts(dict1, dict2, character_list):
    """
    Compare descriptions between two dictionaries for each species.

    Args:
        dict1 (dict): The first dictionary containing species descriptions.
        dict2 (dict): The second dictionary containing species descriptions.
        character_list (str): The character list for reference during comparison.

    Returns:
        None: Prints the comparison results for each species.
    """
    # Iterate through species in the first dictionary
    for species_name in dict1.keys():
        if species_name in dict2:
            # Retrieve descriptions from both dictionaries
            description1 = dict1[species_name]
            description2 = dict2[species_name]

            # Compare the descriptions using the compare_description function
            comparison_result = compare_description(description1, description2, character_list)

            # Print the comparison result
            print(f"Comparison for {species_name}:")
            print(comparison_result)
            print("\n")
        else:
            # Handle case where the species is missing in one of the dictionaries
            print(f"Species {species_name} is missing in the second dictionary.")


# Call the function to compare descriptions
compare_descriptions_between_dicts(species_descriptions_dict, species_descriptions_dict_2, character_list)
