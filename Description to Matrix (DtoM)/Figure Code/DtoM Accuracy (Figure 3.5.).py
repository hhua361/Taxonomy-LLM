import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean data
file_path = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Data-test/2.2 Description to Matrix/Description to Matrix (DtoM accurcy).csv"
data = pd.read_csv(file_path)

# Clean data: Convert percentage strings to numeric values
for col in data.columns[1:]:
    data[col] = data[col].str.rstrip('%').astype(float)

# Prepare heatmap data
dtoM_cols = [col for col in data.columns if 'DtoM' in col]
web_cols = [col for col in data.columns if 'Web' in col]

heatmap_data = data[['Unnamed: 0'] + dtoM_cols + web_cols].copy()
heatmap_data.set_index('Unnamed: 0', inplace=True)

# Split data for DtoM and Web
dtoM_data = heatmap_data[dtoM_cols]
web_data = heatmap_data[web_cols]


# Function to create and save heatmap figures
def save_heatmap_figure(dtom_data, web_data, output_file):
    """
    Create a combined heatmap figure for DtoM and Web methods and save it as an SVG file.

    Parameters:
    dtoM_data (DataFrame): Heatmap data for DtoM methods.
    web_data (DataFrame): Heatmap data for Web methods.
    output_file (str): File path to save the SVG file.
    """
    # Create a combined figure with two subplots for DtoM and Web data side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(20, 8), gridspec_kw={'width_ratios': [1, 1]})

    # Adjusted colormap for DtoM (using a more balanced blue gradient)
    custom_cmap_dtom = sns.light_palette("#C0DAF2", as_cmap=True)

    # Plot DtoM data heatmap on the left
    sns.heatmap(dtom_data, annot=True, fmt='.1f', cmap=custom_cmap_dtom, cbar_kws={'label': 'Accuracy (%)'}, ax=axes[0])
    axes[0].set_title('DtoM Methods Accuracy', fontsize=14, pad=20)
    axes[0].set_xlabel('DtoM Methods', fontsize=12)
    axes[0].set_ylabel('Dataset', fontsize=12)
    axes[0].text(-0.1, 1.05, 'A', transform=axes[0].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')  # Add "A"

    # Custom colormap for Web
    custom_cmap_web = sns.light_palette("#F5A79E", as_cmap=True)

    # Plot Web data heatmap on the right
    sns.heatmap(web_data, annot=True, fmt='.1f', cmap=custom_cmap_web, cbar_kws={'label': 'Accuracy (%)'}, ax=axes[1])
    axes[1].set_title('Web Methods Accuracy', fontsize=14, pad=20)
    axes[1].set_xlabel('Web Methods', fontsize=12)
    axes[1].set_ylabel('')  # Remove ylabel for the second heatmap
    axes[1].text(-0.1, 1.05, 'B', transform=axes[1].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')  # Add "B"

    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig(output_file, format='png', dpi=600)
    print(f"Figure saved to: {output_file}")


# Specify the output file path
output_file = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Figure-Chapter 2/SVG/Figure 2.8.png"

# Call the function to save the heatmap figure
save_heatmap_figure(dtoM_data, web_data, output_file)
