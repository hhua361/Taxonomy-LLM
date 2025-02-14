DtoM (Description to Matrix): Taxonomic Natural Language Processing
====
## Installation
To use the DtoM function, you can download the DtoM.py file located in the main directory. Then, run it in your local Python environment.

DtoM can be installed by following this instruction on Github.\
DtoM depends on the Python package openai, please make sure it is installed as well.

DtoM (Description to Matrix)/DtoM (Description to Matrix).py

 ### Steps:
1. To use the DtoM function, you can download the DtoM.py file located in the main directory. Then, run it in your local Python environment.
2. Ensure you have Python installed on your system.
3. Run the following command in your terminal to execute the file:

```
python path/to/DtoM.py
```
## Obtain the OpenAI API key and configure it as an environment variable
To integrate the TaxonGPT function, the OpenAI API (Application Programming Interface) must be utilized. Connecting to the OpenAI API can invoking relevant models provided by OpenAI. Since the API key is a sensitive and confidential code, it is crucial to prevent exposing the key or submitting it through a browser.To ensure the API key is securely imported and avoid any potential risk, it is mandatory to set the API key as a system environment variable before using the TaxonGPT function.

If the API key is correctly set, the TaxonGPT function will proceed with the subsequent operations. However, if the API key is not properly loaded into the environment, the TaxonGPT function will return an appropriate prompt, providing instructions to help check and resolve the issues.

### How to Correctly Obtain and Use OpenAI's API Key:
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
## Overview
> ### Input file
> DtoM aims to convert unstructured natural language taxonomic descriptions into structured morphological matrices (NEXUS format). In order to obtain comprehensive taxonomic data, the input files of DtoM include:
* **Taxonomic Descriptions** (input_file_path): Contains a natural language taxonomic description, which should include a detailed description of the species
```
This is just an example of the taxonomic description.
##1: Agriphila Hübner
Adults. Face with a conical hairy prominence (this short), or without a conical hairy prominence. Proboscis functional. Wingspan 20–29(–31) mm. The adults conspicuously sexually dimorphic to not very sexually dimorphic. The fringe glistening-metallic, or not glistening-metallic. Termen non-sinuate. Ground colour of the forewings ochreous, or brown, or grey. Forewings plain (sometimes, in A. latistria), or conspicuously patterned with contrasting colours. The patterning complex to simple; restricted to longitudinal streaking, or restricted to transverse markings, or comprising both longitudinal streaking and transverse markings. Forewings with a median line, or without a median line; transversely dark-lined towards the termen (A. geniculea, inconspicuously so in A. inquinatella), or not transversely dark-lined towards the termen; the subterminal lines when present, conspicuously white-edged, or not white-edged; with a strong white median streak, or without a strong white median streak; without conspicuous white marks at or near the apex. Forewing vein 7 arising from vein 8. Hindwings pale ochreous grey, or pale grey to dark grey; plain. Distribution and habitats. Widespread (except the mainland-European A. poliellus, this being included in the British list on the basis of a single specimen taken at Deal, Kent in 1885). England, Wales, Scotland, and Ireland. Occurring in coastal locations and inland. In wet places, mesophytic habitats, and dry places (A. selasella in marshy places including salt marshes and fens; A. geniculea in dry pastures and coastal sand-hills; A. inquinatella in grassy heaths, rough grassland and sandy places; A. latistria in inland heaths with a predilection for burnt patches, also in woodland rides and sandy districts including coastal sand-hills; and A. tristella and A. straminella (formerly Crambus culmellus) common almost throughout the British Isles wherever grass grows). British species: A. geniculea, A. inquinatella, A. latistria, A. geniculea, A. poliellus, A. selasella, A. straminella, A. tristella. Adults abroad July to September. Larvae. Larvae feeding on monocots; Poaceae (Bromus, Festuca, Poa, Deschampsia). Subfamily. Crambinae. ##

##2: Ancylolomia Hübner
Adults. Face without a conical hairy prominence. Proboscis functional. Labial palps short. Wingspan 30–34 mm. Forewings pale ochreous, irrorated grey with a few black scales, with a conspicuous narrow creamy median longitudinal stripe which beyonf the middle bends slightly towards the tornus; a fine yellowish sub-dorsal longitudinal stripe, and creamy striations along the costa and along subterminal veins; a small greyish discal spot; a fine, curved ochreous subterminal line, and a zigzag brown line adorned with silver-metallic scales in the whitish area between this and the termen; the fringe grey, glistening-metallic and incorporating a white line. The fringe not glistening-metallic. Forewing apices somewhat pointed; termen markedly sinuate. Ground colour of the forewings ochreous to brown. Forewings conspicuously patterned with contrasting colours. The patterning complex; comprising both longitudinal streaking and transverse markings (the latter restricted to subterminal lines). Forewings without a median line; transversely dark-lined towards the termen; the subterminal lines conspicuously white-edged; with a strong white median streak (plus streaks on either side); the median streak without a cross-bar; without conspicuous white marks at or near the apex. Forewing vein 7 arising from vein 8. Hindwings pale grey (with a white fringe); plain, or with a subterminal dark line and fuscous termen; very light grey, whiter basally and tending darker towards the termen, marked only by a very fine dark terminal line; the fringe plain white. Distribution and habitats. Found only in southern England (an occasional immigrant from southern Europe). England (E. Kent in 1935, S. Essex in 1996). British species: A. tentaculella. Adults abroad July and August. Larvae. Larvae feeding on monocots; Poaceae. Subfamily. Crambinae. ##

......
```
> ### Usage
>To utilize the TaxonGPT.py file effectively, a configuration file is required. This configuration file should include the necessary input file paths and the output file path. The essential information within the config file includes:
>* **API Key**: Your OpenAI API key.
>* **Paths**: A dictionary containing the paths to the input and output files.
#### You need to put the config file and TaxonGPT.py in the same directory, TaxonGPT.py will automatically recognize the config file
```
This is just an example of the config file format that will be shown.
"""
{
    "api_key": "YOUR API KEY HERE",
    "input_file_path": "<Full path to the input Nexus file>",
    "output_nexus_path": "<Full path to the input Nexus file>"
}
"""
```
To generate taxonomic results efficiently, ensure the configuration file contains the correct file paths. Based on the specific requirements for generating classification results, different branch functions can be used.

## Example
> ### 
> The taxonomic key results generated using the TaxonGPT.Key function are derived from the *Equisetum* dataset extracted from the DELTA database. This dataset includes 12 species characterized by 29 morphological traits, stored in the form of a Nexus matrix.

```markdown
#NEXUS
BEGIN DATA;
DIMENSIONS NTAX=15 NCHAR=14;

[! This is an automatically generated NEXUS matrix for phylogenetic analysis.]
FORMAT MISSING=? GAP=- SYMBOLS="123456";

CHARLABELS
[1] 'Presence of conical hairy prominence on face'
[2] 'Proboscis functionality'
[3] 'Sexual dimorphism in adults'
[4] 'Fringe appearance'
[5] 'Termen shape'
[6] 'Ground colour of forewings'
[7] 'Forewing patterning complexity'
[8] 'Forewing patterning type'
[9] 'Presence of median line on forewings'
[10] 'Transverse dark lines towards termen on forewings'
[11] 'Presence of strong white median streak on forewings'
[12] 'Presence of conspicuous white marks at or near the apex of forewings'
[13] 'Forewing vein 7 connection'
[14] 'Hindwing colour'
;

STATELABELS
1 'Present' 'Absent',
2 'Functional' 'Atrophied',
3 'Conspicuously sexually dimorphic' 'Not very sexually dimorphic',
4 'Glistening-metallic' 'Not glistening-metallic' 'Conspicuously chequered' 'Somewhat chequered' 'Not chequered',
5 'Non-sinuate' 'Sinuate' 'Somewhat sinuate',
6 'Ochreous' 'Brown' 'Grey' 'Whitish' 'Dark fuscous' 'Ferrugineous brown',
7 'Plain' 'Inconspicuously patterned' 'Conspicuously patterned' 'Very conspicuously patterned',
8 'Longitudinal streaking' 'Transverse markings' 'Both longitudinal streaking and transverse markings' 'Dark dots',
9 'Present' 'Absent',
10 'Present' 'Absent',
11 'Present' 'Absent',
12 'Present' 'Absent',
13 'Arising from vein 8' 'Free',
14 'Pale grey' 'Dark grey' 'White' 'Whitish' 'Ochreous whitish' 'Pale fuscous' 'Dark fuscous';

MATRIX
'Species 1' (1 2) 1 (1 2) (1 2) 1 (1 2 3) (1 3) 3 (1 2) (1 2) (1 2) 2 1 (1 2)
'Species 2' 2 1 - 2 2 1 3 3 2 1 1 2 1 1
'Species 3' 2 2 (1 2) (2 3) 1 3 2 4 2 2 2 2 1 3
'Species 4' 2 1 - (2 3 4 5) 1 (1 2 3) 3 3 2 (1 2) (1 2) (1 2) 1 (1 2)
'Species 5' 1 1 1 2 (2 3) 1 (1 2) 3 2 2 2 2 2 (3 4 5)
'Species 6' 2 1 - 1 1 4 4 3 1 2 2 2 1 (1 2)
'Species 7' 2 1 - 1 1 (1 2) 3 3 2 1 2 2 1 (1 2 6)
'Species 8' 2 1 - (1 2) (1 2) (1 2 4) (1 3) 3 2 (1 2) (1 2) (1 2) 1 (1 2 4)
'Species 9' 2 2 1 2 3 (1 2) (2 3) (1 2) 2 (1 2) 2 2 - (4 5 6)
'Species 10' 1 1 - 2 1 (1 2) (2 3) (2 3) 2 1 2 2 2 (1 4)
'Species 11' 1 1 1 (2 4 5) 1 (1 2) 3 (2 3) 2 2 2 2 2 4
'Species 12' 2 1 (1 2) 2 (1 2) (1 4 5) (1 3) 3 1 1 2 2 1 (1 4 6 7)
'Species 13' 2 1 (1 2) (1 2) (1 2) 2 (1 2) 1 (1 2) 1 1 2 2 (1 2 6 7)
'Species 14' 2 2 1 2 3 (1 2 3) 2 (1 4) 2 2 2 2 - (3 4 5)
'Species 15' 2 1 - 1 1 6 3 3 1 1 2 2 1 (1 2)
;
END;
```
