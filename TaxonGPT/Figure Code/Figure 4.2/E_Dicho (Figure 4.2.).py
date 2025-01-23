import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "E:/Evaluate_results_for_all_datasets/Evaluate_table/E_Dicho/E_Dicho_simplify.csv"
data = pd.read_csv(file_path)

# Select the required columns and rename them
df = data[['Dataset/time', 'E_DichoAPI (average)', 'E_DichoWEB (average)', 'E_DichoDELTA']]
df.columns = ['Dataset', 'API', 'Web', 'Delta']

# Set the index to the 'Dataset' column
df.set_index('Dataset', inplace=True)

# Remove rows containing NaN values
df_cleaned = df.dropna()

# Ensure scores are rounded to three decimal places
df_cleaned = df_cleaned.round(3)

# Create a light transparent color gradient using sns.light_palette
# Deeper colors represent higher scores
cmap = sns.light_palette("#F5A79E", as_cmap=True)

# Configure the figure size and font settings
plt.figure(figsize=(14, 6))
sns.set(font='Arial')

# Create the heatmap
ax = sns.heatmap(
    df_cleaned,
    annot=True,
    fmt=".3f",
    cmap=cmap,
    cbar_kws={'orientation': 'vertical', 'shrink': 0.8},
    annot_kws={"fontsize": 18, "color": "black", "fontname": "Arial"}
)

# Add title and axis labels, and set their fonts
plt.title('Comparison of Ways on Different Datasets', fontsize=22, fontname='Arial', pad=20)
plt.xlabel('Methods', fontsize=20, fontname='Arial')
plt.ylabel('Datasets', fontsize=20, fontname='Arial')

# Configure tick labels and their fonts
ax.set_xticklabels(ax.get_xticklabels(), fontsize=18, fontname='Arial', rotation=0)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=16, fontname='Arial')

# Customize tick parameters
ax.tick_params(left=True, bottom=True, length=10, width=2, colors='black', grid_color='black', grid_alpha=0.5, pad=10)

# Ensure only the left and bottom borders are visible
for spine_location, spine in ax.spines.items():
    if spine_location in ['left', 'bottom']:
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(1.5)
    else:
        spine.set_visible(False)

# Adjust the color bar position and tick labels
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=16, labelcolor='black')
cbar.ax.set_yticklabels(cbar.ax.get_yticklabels(), fontsize=16, fontname='Arial')

# Add a label to the color bar at the top
cbar.ax.set_title('E_Dicho', fontsize=18, fontname='Arial', pad=10)

# Save the figure in SVG format
output_path = 'E:/Evaluate_results_for_all_datasets/Evaluate_table/E_Dicho/Comparison_heatmap.svg'
plt.savefig(output_path, format='svg', dpi=600)

# Display the plot
plt.tight_layout()
plt.show()
