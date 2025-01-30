UoA - Master of science - Thesis
====

# Investigating the Application of Generative Artifical Intelligence in Taxonomy

## Abstract
Taxonomy is essential for biological sciences but remains a labor-intensive process that heavily depends on expert knowledge. The advent of large language models (LLMs) presents an opportunity to automate and enhance taxonomic workflows, reducing subjectivity and improving efficiency. This study explores the application of LLMs in taxonomy through two key AI-driven pipelines: DtoM (Description to Matrix) and TaxonGPT, both designed to improve taxonomic description processing, species classification, and taxonomic key generation.

DtoM is a structured pipeline that extracts morphological characters from unstructured taxonomic descriptions and converts them into structured matrices, improving interoperability with existing taxonomic databases. TaxonGPT is an LLM-powered classification system that employs retrieval-augmented generation (RAG) and knowledge graph-based prompting to enhance contextual accuracy while minimizing AI hallucinations. The performance of these models was evaluated using 11 real-world taxonomic datasets, comparing their accuracy, efficiency, and reproducibility against conventional methods.

Results indicate that DtoM achieves near-perfect accuracy (>99%) in morphological character extraction, significantly outperforming traditional manual-based workflows​. Meanwhile, TaxonGPT consistently generated correct taxonomic keys with 100% accuracy, exceeding the web-based GPT-4o model (79.9% accuracy for complex datasets)​. In terms of efficiency, TaxonGPT’s classification speed correlates with dataset complexity, but remains computationally viable, with taxonomic key generation costing under $1 per dataset​. Additionally, incorporating knowledge graphs improved semantic understanding, enhancing classification accuracy, particularly in complex datasets​.

Despite these advancements, challenges persist in model interpretability, domain-specific biases, and computational costs associated with scaling LLM-driven taxonomy. This study provides a foundation for AI-powered taxonomy, demonstrating the feasibility of LLMs in automating taxonomic tasks while maintaining high accuracy. The findings suggest that integrating AI with expert-driven workflows can significantly accelerate biodiversity research, facilitate large-scale taxonomic data standardization, and support conservation efforts.

**Keywords: Taxonomy, Large Language Models, Generative AI, Knowledge Graphs, Retrieval-Augmented Generation, Species Classification, TaxonGPT, DtoM, AI Taxonomic Workflows**

## Outline:
All experimental tests and simulations were conducted using the Python programming language within the PyCharm integrated development environment (IDE) and web-based LLM platforms. The execution process involved multiple software tools and programming languages, including Python, Linux, and R (for scripting), as well as command-line interfaces for executing scripts.
> ### Software and Tools Used
> The primary software used includes:
*  **Large Language Models (LLMs)**: Selected LLMs for taxonomic tasks
*  **PAUP**: Software for phylogenetic analysis
*  **Mesquite**: Taxonomic software for evolutionary biology
*  **DELTA**: A descriptive language tool for taxonomic data

> ### Code Organization and Figure Generation
> Benchmarking results and visualization scripts for different pipelines are stored in the following directories:
* **TaxonGPT**: TaxonGPT/Figure_code
* **Simulation Test**: Simulation Test/Figure_code
* **DtoM (Description to Matrix)**: DtoM/Figure_code

For Simulation Test, DtoM (Description to Matrix), and TaxonGPT, we utilized OpenAI's ChatGPT-4o (2024/08/06) via API calls. Before running these scripts, users must configure their local environment by importing an OpenAI API key to enable model access. To set up the API key, add the following in your environment configuration:
> ### Obtain the OpenAI API key and configure it as an environment variable
To integrate the TaxonGPT function, the OpenAI API (Application Programming Interface) must be utilized. Connecting to the OpenAI API can invoking relevant models provided by OpenAI. Since the API key is a sensitive and confidential code, it is crucial to prevent exposing the key or submitting it through a browser.To ensure the API key is securely imported and avoid any potential risk, it is mandatory to set the API key as a system environment variable before using the TaxonGPT function.

If the API key is correctly set, the TaxonGPT function will proceed with the subsequent operations. However, if the API key is not properly loaded into the environment, the TaxonGPT function will return an appropriate prompt, providing instructions to help check and resolve the issues.

#### How to Correctly Obtain and Use OpenAI's API Key:
1. Locate the "API" section at the bottom of the OpenAI interface.
2. Log in to your user account through the API login portal and navigate to the API interface.
3. Click on the "Dashboard" located at the top right corner.
4. Access the "API keys" interface to manage your API keys.
5. Create the API key and ensure to save and record this key properly for future use.


![step1-4](https://github.com/user-attachments/assets/b17b1c8e-d233-40e4-a0dd-c8a8683bdde1)

*** Once you have obtained the API code from OpenAI, the first step is to configure the API within the environment variables. This can be done by executing the appropriate configuration commands in PowerShell. After successfully configuring the API in the environment, it is essential to restart the terminal window to ensure that the changes take effect, and then use the relevant commands to verify the environment variables.
```
# For configuring environment variables (API) in PowerShell. (For Windows)
setx OPENAI_API_KEY “YOUR_API_KEY”
# Verifying whether the environment variables (API) were successfully imported in the new PowerShell session. (For Windows)
$env:OPENAI_API_KEY

# For configuring environment variables (API) in PowerShell. (For Linux/macOS)
export OPENAI_API_KEY="sk-your-api-key"
# Verifying whether the environment variables (API) were successfully imported in the new PowerShell session. (For Linux/macOS)
echo $OPENAI_API_KEY
```
#### ⚠️Caution: Refrain from disclosing your API key to unauthorized individuals or posting it in publicly accessible locations.

## Installation and Usage
> ### Simulation Test
To run each simulation, the three simulation processes are located in the Simulation Test folder. Before executing the simulation scripts, ensure that the required Python packages, including json, OpenAI, os, random, typing, and re, are installed in your environment. For further inspection or modification of the prompts used in model invocation within the pipeline, open the corresponding Python script using a compatible Python IDE such as PyCharm or VS Code to ensure proper execution and editing.
> ### DtoM (Description to Matrix)
The code for the DtoM (Description to Matrix) module is stored in the DtoM (Description to Matrix) folder. Before running the script, ensure that the required Python packages, including json, OpenAI, os, and re, are installed in your environment. To process taxonomic descriptions, replace the file_path variable in the script with the path to the TXT file containing the taxonomic description to be analyzed. 

For further inspection or modification of the prompts used in model invocation within the pipeline, open the corresponding Python script using a compatible Python IDE such as PyCharm or VS Code to ensure proper execution and editing.
> ### TaxonGPT
The code for TaxonGPT is stored in the TaxonGPT folder. Before running the script, ensure that the required Python packages, including json, OpenAI, os, re, and pandas, are installed in your environment. In the config file, update the file paths to match the corresponding input data locations. Additionally, the prompts used for model invocation are stored separately in TaxonGPT/Prompt_messages.json, allowing users to review and modify them as needed.

To utilize the TaxonGPT.py file effectively, a configuration file is required. This configuration file should include the necessary input file paths and the output file path. The essential information within the config file includes:
#### Input file
TaxonGPT is dedicated to converting information from Nexus matrices into biologically meaningful taxonomic information and accurate natural language descriptions of species. To achieve comprehensive taxonomic data, the input files for TaxonGPT include:
* **Nexus Matrix** (nexus_file_path): Contains species and their corresponding character states.
* **Prompt Message** (prompt_file_path): Instructions for the API model. This file can be adjusted based on specific requirements.
* **Character Information** (character_file_path): Since the matrix typically lacks detailed descriptions, character mapping is necessary to obtain taxonomically meaningful descriptions.

#### Output file
There are many types of outputs that can be generated by using TaxonGPT:
* **Csv file** (csv_output_path): Store and output Nexus matrix information in csv format.
* **Knowledge graph file** (prompt_file_path): The Nexus matrix information is stored and output in the knowledge graph format.
* **Taxonomic description** (taxonomic_description_path): Output the taxonomic description corresponding to the Nexus matrix content.
* **Taxonomic key** (taxonomic_key_path): Output the taxonomic key corresponding to the Nexus matrix content.
  
To utilize the TaxonGPT.py file effectively, a configuration file is required. This configuration file should include the necessary input file paths and the output file path. The essential information within the config file includes:
* **API Key**: Your OpenAI API key.
* **Paths**: A dictionary containing the paths to the input and output files.
```python
{
    "api_key": "YOUR API KEY HERE",
    "nexus_file_path": "<Full path to the input Nexus file>",
    "prompt_file_path": "<Full path to the input Prompt file>",
    "character_file_path": "<Full path to the input character info file>",
    
    "csv_output_path": "<Full path to  output CSV format matrix file>",
    "json_output_path": "<Full path to output JSON format matrix file>",
    "taxonomic_description_path": "<Full path to output taxonomic description file>"
    "taxonomic_key_path": "<Full path to output taxonomic key file>"

    
    "comparison_output_path": "<Full path to output taxonomic key file>",
    # By default, the description check feature is disabled to prevent generating excessive redundant results. If you need to check the execution steps, please set "enable_description_check": false to true in the configuration file.
    "enable_description_check": false

}
```
TaxonGPT consists of two main functionalities: DESCRIBE and KEY. Users can select and execute these functions within the Python script by specifying the desired task:
```python
# Through TaxonGPT() to generate the related result
TaxonGPT = TaxonGPT(config_file_path)

# Generate the Taxonomic Key
TaxonGPT.process_key()

# Generate the Taxonomic Description
TaxonGPT.process_description()
```
These functions can be executed through the TaxonGPT instance, ensuring proper data processing and taxonomic classification.

## Timeline
This timeline provides a comprehensive overview of the research phases undertaken throughout 2024, detailing the various experimental procedures, iterations, and technological advancements at each stage. The project focuses on applying Generative Artificial Intelligence (AI) to taxonomy, aiming to enhance taxonomic classification and morphological matrix processing through AI-driven methodologies. The research is systematically divided into three primary phases, each addressing distinct technical challenges and refining AI-assisted taxonomic processes.

![Taxon-GPT-Timeline](https://github.com/user-attachments/assets/b12e762f-d8df-4ae0-9089-6249d6fb2351)

> ### Timeline Outline
*  **February 28, 2024 – June 12, 2024: Pre-Test Module** This phase primarily focused on conducting pre-tests to assess the applicability of Large Language Models (LLMs) in taxonomic research. The initial steps involved selecting appropriate taxonomic datasets, evaluating different LLMs for their suitability, and designing experimental workflows. During this phase, key challenges such as AI hallucination and data processing limitations were identified. Various techniques, including knowledge graphs and prompt engineering, were explored to mitigate these issues. Additionally, preliminary tests were conducted to assess the accuracy of AI-assisted taxonomic descriptions and classifications. The findings from this stage provided critical insights that guided the refinement of AI models in later phases.
-  **June 14, 2024 – October 11, 2024: TaxonGPT – Taxonomic Classification with Generative AI**: Building upon the insights gained from the pre-test module, this phase aimed to integrate AI models into concrete taxonomic classification tasks. The focus was on improving model accuracy, reducing AI-induced errors, and optimizing data processing workflows. A major outcome of this phase was the development of a pipeline capable of converting morphological matrices into taxonomic descriptions and taxonomic keys. Key methodologies, such as distributed execution, recursive design, and context-aware processing, were incorporated to enhance result accuracy and reproducibility. This phase also involved manuscript preparation and submission to academic journals for peer review, ensuring the scientific rigor of the proposed methodologies.
*  **August 12, 2024 – November 12, 2024: DtoM – Taxonomic Natural Language Processing**: In the final phase, the research shifted focus to developing an advanced AI-driven "Description to Matrix" (DtoM) process. This involved designing multiple simulation-based experiments to optimize pipeline construction, refine the coding framework, and improve workflow efficiency. The iterative design process helped minimize AI hallucination and enhance result reproducibility. By integrating Retrieval-Augmented Generation (RAG) and recursive design strategies, the final DtoM system was successfully developed and validated. The outcomes of this phase were documented in a thesis, culminating in a comprehensive study on AI-driven taxonomy.


## Results Eaxample
Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text.

## Acknowledgements
Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text.
