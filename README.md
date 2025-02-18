UoA - Master of science - Thesis
====

# Investigating the Application of Generative Artifical Intelligence in Taxonomy

## Abstract
Taxonomy plays a crucial role in biological research by offering foundational data for numerous scientific disciplines. However, limited resources, ecological shifts, and vast undiscovered species data pose a severe challenge, termed the 'Taxonomic Impediment'. This encompasses uneven distribution of taxonomic resources, lack of unified data formats, difficulties balancing naming efficiency and data quality, and a heavy reliance on expert knowledge and manual labor. The recent rapid development of Artificial Intelligence (AI), especially Large Language Models (LLMs), presents new opportunities for streamlining taxonomic workflows, given the extensive natural language involved in taxonomy study.

This study investigate the applications of LLM in taxonomy and constructs LLM-based research pipelines to demonstrate their practical potential. The research includes three main components: (1) a Pilot Test (Chapter 2) to select relevant taxonomic data types, assess current LLM potential, and explore how Prompt Engineering and Knowledge Graph (KG) techniques integrate with LLM-based taxonomic tasks; (2) the Description to Matrix (DtoM) pipeline (Chapter 3), which employs ChatGPT-4o in a Python environment to automatically extract morphological traits from unstructured descriptions and convert them into structured data matrices; and (3) TaxonGPT (Chapter 4), which extends LLM usage by automatically generating taxonomic descriptions and identification keys from NEXUS-formatted morphological matrices, incorporating knowledge graphs and error-checking modules to reduce “hallucinations” and boost accuracy.

Experimental results show that DtoM efficiently and accurately converts unstructured taxonomic descriptions into structured matrices across multiple real-world datasets. TaxonGPT further demonstrates the broad potential of LLMs in taxonomy, with benchmark results confirming notable performance in accuracy, efficiency, and reproducibility. Despite these promising findings, issues such as limited model interpretability, domain-specific biases, and substantial computational costs persist. Future work may focus on enhancing LLM controllability and stability for more reliable large-scale taxonomic research. As an exploratory AI-driven effort, this study validates the feasibility of allowing LLMs to perform taxonomy tasks automatically while maintaining high accuracy, laying a foundation for more comprehensive intelligent taxonomy research.

**Keywords: Taxonomy, Large Language Models (LLMs), Artificial Intelligence (AI), generative AI (gAI), Knowledge Graphs (KG), Retrieval-Augmented Generation(RAG)**

## Timeline
This timeline provides a comprehensive overview of the research phases undertaken throughout 2024, detailing the various experimental procedures, iterations, and technological advancements at each stage. The project focuses on applying Generative Artificial Intelligence (AI) to taxonomy, aiming to enhance taxonomic classification and morphological matrix processing through AI-driven methodologies. The research is systematically divided into three primary phases, each addressing distinct technical challenges and refining AI-assisted taxonomic processes.

![Taxon-GPT-Timeline](https://github.com/user-attachments/assets/b12e762f-d8df-4ae0-9089-6249d6fb2351)

> ### Timeline Outline
*  **February 28, 2024 – June 12, 2024: Pre-Test Module** This phase primarily focused on conducting pre-tests to assess the applicability of Large Language Models (LLMs) in taxonomic research. The initial steps involved selecting appropriate taxonomic datasets, evaluating different LLMs for their suitability, and designing experimental workflows. During this phase, key challenges such as AI hallucination and data processing limitations were identified. Various techniques, including knowledge graphs and prompt engineering, were explored to mitigate these issues. Additionally, preliminary tests were conducted to assess the accuracy of AI-assisted taxonomic descriptions and classifications. The findings from this stage provided critical insights that guided the refinement of AI models in later phases.
-  **June 14, 2024 – October 11, 2024: TaxonGPT – Taxonomic Classification with Generative AI**: Building upon the insights gained from the pre-test module, this phase aimed to integrate AI models into concrete taxonomic classification tasks. The focus was on improving model accuracy, reducing AI-induced errors, and optimizing data processing workflows. A major outcome of this phase was the development of a pipeline capable of converting morphological matrices into taxonomic descriptions and taxonomic keys. Key methodologies, such as distributed execution, recursive design, and context-aware processing, were incorporated to enhance result accuracy and reproducibility. This phase also involved manuscript preparation and submission to academic journals for peer review, ensuring the scientific rigor of the proposed methodologies.
*  **August 12, 2024 – November 12, 2024: DtoM – Taxonomic Natural Language Processing**: In the final phase, the research shifted focus to developing an advanced AI-driven "Description to Matrix" (DtoM) process. This involved designing multiple simulation-based experiments to optimize pipeline construction, refine the coding framework, and improve workflow efficiency. The iterative design process helped minimize AI hallucination and enhance result reproducibility. By integrating Retrieval-Augmented Generation (RAG) and recursive design strategies, the final DtoM system was successfully developed and validated. The outcomes of this phase were documented in a thesis, culminating in a comprehensive study on AI-driven taxonomy.

## Outline:
All experimental tests and simulations were conducted using the Python programming language within the PyCharm integrated development environment (IDE) and web-based LLM platforms. The execution process involved multiple software tools and programming languages, including Python, Linux, and R (for scripting), as well as command-line interfaces for executing scripts. **Please refer to the [Wiki](https://github.com/hhua361/UoA-Thesis/wiki/Overview) for an overview of the project.** 

> ### Software and Tools Used
> The primary software used includes:
*  **Large Language Models (LLMs)**: Selected LLMs for taxonomic tasks
*  **PAUP (version 4.0)**: Software for phylogenetic analysis
*  **Mesquite (version 3.12)**: Taxonomic software for evolutionary biology
*  **DELTA**: A descriptive language tool for taxonomic data

> ### Code Organization and Figure Generation
> Benchmarking results and visualization scripts for different pipelines are stored in the following directories:
* **TaxonGPT**: TaxonGPT/Figure_code
* **Simulation Test**: Simulation Test/Figure_code
* **DtoM (Description to Matrix)**: DtoM/Figure_code

For Simulation Test, DtoM (Description to Matrix), and TaxonGPT, we utilized OpenAI's ChatGPT-4o (2024/08/06) via API calls. Before running these scripts, users must configure their local environment by importing an OpenAI API key to enable model access. To set up the API key, add the following in your environment configuration:
> ### Obtain OpenAI API key and set as environment variable
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
```python
# Define the path to the file containing species descriptions
file_path = "species_descriptions.txt"
```
For further inspection or modification of the prompts used in model invocation within the pipeline, open the corresponding Python script using a compatible Python IDE such as PyCharm or VS Code to ensure proper execution and editing. For details, please refer to: Vignettes/DtoM.md
> ### TaxonGPT
The code for TaxonGPT is stored in the TaxonGPT folder. Before running the script, ensure that the required Python packages, including json, OpenAI, os, re, and pandas, are installed in your environment. In the config file, update the file paths to match the corresponding input data locations. Additionally, the prompts used for model invocation are stored separately in TaxonGPT/Prompt_messages.json, allowing users to review and modify them as needed. For details, please refer to: Vignettes/TaxonGPT.md

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

## Results Eaxample
> ### DtoM (Description to Matrix)
> > **NEXUS Matrix**: The NEXUS matrix generated using the DtoM (Description to Matrix) pipeline is from the Ephemeroptera dataset extracted from the DELTA database. This dataset includes 6 species with 28 morphological characters, using Taxonomic description as input.
```markdown
#NEXUS
BEGIN DATA;
DIMENSIONS NTAX=5 NCHAR=10;

[! This is an automatically generated NEXUS matrix for phylogenetic analysis.]
FORMAT MISSING=? GAP=- SYMBOLS="1234";

CHARLABELS
[1] 'Compound eyes shape and structure'
[2] 'Fore-wing vein R5 and R4 connection'
[3] 'Presence of hind-wings'
[4] 'Hind-wing length relative to fore-wing in females'
[5] 'Hind-wing costa structure'
[6] 'Number of moveable segments in hind tarsi'
[7] 'Number of tails on the abdomen'
[8] 'Position of gills in nymphs'
[9] 'Fringing of gills with filaments'
[10] 'Fore-leg insertion under the thorax'
;

STATELABELS
1 'Contiguous (males), rounded (females)' 'Two-lobed (males), rounded (females)' 'Rounded',
2 'Joined basally' 'Detached basally',
3 'Present' 'Absent',
4 'More than one fifth the length' 'No more than one fifth the length',
5 'Smoothly curved' 'With a conspicuous projection',
6 '4 segments' '2-3 segments',
7 'Two tails' 'Three tails',
8 'Mostly at the sides of the abdomen' 'Mostly on the upper surface of the abdomen',
9 'Not fringed with filaments on both sides' 'Never comprising a plate bearing a tuft of filaments',
10 'Widely separated' 'Relatively close together';

MATRIX
'Baetis Leach'
2 2 1 2 (1 2) 1 1 1 (1 2) -
'Brachycercus Curtis'
3 1 2 2 - 1 2 2 1 1
'Caenis Stephens'
3 1 2 - - 1 2 2 1 2
'Centroptilum Eaton'
2 2 1 2 2 1 1 1 1 -
'Cloeon Leach'
3 2 2 1 - 1 1 1 1 -
;
END;
```
> ### TaxonGPT
> **Taxonomic Key**: The taxonomic key results generated using the TaxonGPT.Key function are derived from the Equisetum dataset extracted from the DELTA database. This dataset includes 12 species characterized by 29 morphological traits, stored in the form of a Nexus matrix.
```markdown
1.
    -  The rhizomes <whether tuberous>: Bearing tubers ........ 2
    -  The rhizomes <whether tuberous>: Bearing tubers//Not tuberous ........ 3
    -  The rhizomes <whether tuberous>: Not tuberous ........ 4
2(1).
    -  The longitudinal internodal grooves <in the main stem internodes of the assimilating shoots, details>: Fine, the ribs between them not prominent ........ 5
    -  The longitudinal internodal grooves <in the main stem internodes of the assimilating shoots, details>: Deep, with prominent ridges between ........ Equisetum palustre
3(1).
    -  The shoots <dimorphism>: Conspicuously dimorphic ........ 7
    -  The shoots <dimorphism>: Distinguishable as fertile and sterile ........ Equisetum sylvaticum
    -  The shoots <dimorphism>: All green and alike vegetatively, the sterile and cone-bearing shoots emerging at the same time ........ Equisetum fluviatile
4(1).
    -  The main stems <of the assimilating shoots, persistence>: Persisting through the winter ........ 8
    -  The main stems <of the assimilating shoots, persistence>: Dying down in autumn ........ 9
5(2).
    -  Endodermis <in main stem internodes of assimilating shoots, location>: Surrounding the individual vascular bundles ........ 6
    -  Endodermis <in main stem internodes of assimilating shoots, location>: Comprising a single layer outside the ring of vascular bundles ........ Equisetum palustre
6(5).
    -  The main stems <of the assimilating shoots, carriage>: Erect ........ Equisetum litorale
    -  The main stems <of the assimilating shoots, carriage>: Erect//Decumbent ........ Equisetum palustre
7(3).
    -  The brown, non-assimilating fertile stems <number of sheaths>: With numerous sheaths and relatively short internodes ........ Equisetum telmateia
    -  The brown, non-assimilating fertile stems <number of sheaths>: With only 4 to 6 relatively distant sheaths ........ Equisetum arvense
8(4).
    -  The main stems <of the assimilating shoots, branching>: Bearing whorls of slender branches at the nodes ........ Equisetum ramosissimum
    -  The main stems <of the assimilating shoots, branching>: Sparingly branched, the branches solitary and similar to the main stem//Simple ........ 10
    -  The main stems <of the assimilating shoots, branching>: Simple ........ Equisetum hyemale
9(4).
    -  The shoots <dimorphism>: Distinguishable as fertile and sterile ........ Equisetum pratense
    -  The shoots <dimorphism>: All green and alike vegetatively, the sterile and cone-bearing shoots emerging at the same time ........ Equisetum moorei
10(8).
    -  The main stems <of the assimilating shoots, rough or smooth>: Very rough ........ Equisetum trachyodon
    -  The main stems <of the assimilating shoots, rough or smooth>: Slightly rough ........ Equisetum variegatum
```
> **Taxonomic Description**: The dataset results generated using the TaxonGPT. Description function include detailed information for one of the species, *Equisetum arvense*. This data is derived from the *Equisetum* dataset extracted from the DELTA database, which comprises 12 species characterized by 29 morphological characters, stored in the form of a Nexus matrix.
```
Taxonomic Description for *Equisetum arvense*
Equisetum_arvense: 
	List Form:
	1. **The rhizomes**: Bearing tubers and Not tuberous
	2. **The shoots**: Conspicuously dimorphic
	3. **The brown, non-assimilating fertile stems**: With only 4 to 6 relatively distant sheaths
	4. **The main stems (of the assimilating shoots, carriage)**: Erect and Decumbent
	5. **The main stems (of the assimilating shoots, colour)**: Bright green
	6. **The main stems (of the assimilating shoots, rough or smooth)**: Slightly rough
	7. **The main stems (of the assimilating shoots, branching)**: Bearing whorls of slender branches at the nodes
	8. **The main stems (of the assimilating shoots, persistence)**: Dying down in autumn
	9. **The main stem internodes (of the assimilating shoots, whether swollen)**: Missing
	10. **The longitudinal internodal grooves (in the main stem internodes of the assimilating shoots, details)**: Deep,with prominent ridges between
	11. **The main stem internodes (of the assimilating shoots, presence of a central hollow)**: With a central hollow
	12. **Central hollow (of the main stem internodes of assimilating shoots, relative diameter)**: Much less than half the diameter of the internode and About half the diameter of the internode
	13. **Endodermis (in main stem internodes of assimilating shoots, location)**: Comprising a single layer outside the ring of vascular bundles
	14. **The main stem sheaths (of assimilating shoots, length relative to breadth)**: About as broad as long
	15. **The main stem sheaths (of assimilating shoots, loose or appressed)**: Missing
	16. **The teeth (of the main stem sheaths of assimilating shoots, ribbing)**: Ribbed
	17. **The teeth (of the main stem sheaths of assimilating shoots, persistence)**: Missing
	18. **The primary branching (regularity)**: Symmetrical
	19. **The primary branches (when present, few or many)**: Numerous
	20. **The primary branches (carriage)**: Spreading and Drooping
	21. **The primary branches (of assimilating shoots, whether themselves branched)**: Simple
	22. **The first (primary) branch internodes (of assimilating shoots, relative length)**: At least as long as the subtending sheaths, at least on the upper parts of the stem
	23. **The primary branch internodes**: Solid
	24. **Stomata (of assimilating shoots, insertion relative to the adjacent epidermal cells)**: Not sunken
	25. **The cones (blunt or apiculate)**: Blunt
	26. **Spores (whether fertile)**: Fertile
	27. **Spores released (months released)**: April
	28. **Subgenus**: Equisetum
	29. **Section (of subgenus Equisetum)**: Vernalia
	
	Paragraph Form:
	Equisetum arvense is characterized by rhizomes that are both bearing tubers and not tuberous (1). The shoots are conspicuously dimorphic (2). The brown, non-assimilating fertile stems have only 4 to 6 relatively distant sheaths (3). The main stems of the assimilating shoots are both erect and decumbent (4), and they are bright green in color (5). These stems are slightly rough (6) and bear whorls of slender branches at the nodes (7). The main stems die down in autumn (8). The longitudinal internodal grooves in the main stem internodes of the assimilating shoots are deep, with prominent ridges between (10). The main stem internodes have a central hollow (11), which is much less than half the diameter of the internode and about half the diameter of the internode (12). The endodermis in the main stem internodes of the assimilating shoots comprises a single layer outside the ring of vascular bundles (13). The main stem sheaths of the assimilating shoots are about as broad as long (14). The teeth of the main stem sheaths of the assimilating shoots are ribbed (16). The primary branching is symmetrical (18), and the primary branches are numerous (19). These branches are both spreading and drooping (20). The primary branches of the assimilating shoots are simple (21), and the first primary branch internodes are at least as long as the subtending sheaths, at least on the upper parts of the stem (22). The primary branch internodes are solid (23). The stomata of the assimilating shoots are not sunken relative to the adjacent epidermal cells (24). The cones are blunt (25). The spores are fertile (26) and are released in April (27). This species belongs to the subgenus Equisetum (28) and the section Vernalia (29).
```

## Acknowledgements
Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text.
