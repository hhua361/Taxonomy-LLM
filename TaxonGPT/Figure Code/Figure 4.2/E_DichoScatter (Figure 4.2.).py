import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = "E:/Evaluate_results_for_all_datasets/Evaluate_table/E_Dicho/E_Dicho_scatter.csv"
data = pd.read_csv(file_path)

# Clean and organize data by processing experiment results for each dataset
api_data = data.melt(id_vars=['Dataset/time'],
                     value_vars=['E_DichoAPI1', 'E_DichoAPI2', 'E_DichoAPI3', 'E_DichoAPI4', 'E_DichoAPI5'],
                     var_name='Trial', value_name='Runtime')
api_data['Method'] = 'API'

web_data = data.melt(id_vars=['Dataset/time'],
                     value_vars=['E_DichoWEB1', 'E_DichoWEB2', 'E_DichoWEB3', 'E_DichoWEB4', 'E_DichoWEB5'],
                     var_name='Trial', value_name='Runtime')
web_data['Method'] = 'Web'

delta_data = data.melt(id_vars=['Dataset/time'],
                       value_vars=['E_DichoDELTA'],
                       var_name='Trial', value_name='Runtime')
delta_data['Method'] = 'DELTA'

# Combine API, Web, and DELTA data
combined_data = pd.concat([api_data, web_data, delta_data])

# Rename columns
combined_data.rename(columns={'Dataset/time': 'Dataset'}, inplace=True)

# Replace "Na" string with NaN
combined_data['Runtime'] = combined_data['Runtime'].replace("Na", pd.NA)

# Convert the 'Runtime' column to numeric and handle non-numeric values
combined_data['Runtime'] = pd.to_numeric(combined_data['Runtime'], errors='coerce')

# Drop rows with NA values
combined_data.dropna(subset=['Runtime'], inplace=True)

# Check column names
print(combined_data.columns)

# Set font
plt.rcParams["font.family"] = "Arial"

# Set style
sns.set(style="whitegrid")

# Define colors
palette = {
    'API': '#EF7A6D',
    'Web': '#9DC3E7',
    'DELTA': '#7FB77E'
}

scatter_palette = [
    '#FF9999', '#FFB3B3', '#FFD9D9', '#FFE5E5',  # Modified light red shades
    '#2E75B6',  # Added darker blue
    '#9DC3E7', '#AED8F0', '#ADD8E6', '#BFECF9', '#D0F0FF', '#E0F7FF'  # Light blue shades
]

# Create violin and scatter plot
plt.figure(figsize=(14, 8))

# Draw violin plot
ax = sns.violinplot(data=combined_data, x='Method', y='Runtime', hue='Method',
                    palette=palette, inner=None, linewidth=2, legend=False)

# Remove fill colors
for collection in ax.collections:
    collection.set_facecolor('none')

# Draw scatter plot
sns.stripplot(data=combined_data, x='Method', y='Runtime', hue='Dataset',
              dodge=True, jitter=0.2, marker='o', alpha=1, linewidth=1, palette=scatter_palette, s=15)

# Adjust legend
legend = plt.legend(title='Dataset', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=14, title_fontsize=16)
plt.setp(legend.get_title(), family='Arial')  # Set legend title font
for text in legend.get_texts():
    text.set_family('Arial')  # Set legend label font

# Set plot title and labels
plt.title('Comparison of E_Dicho between API, Web, and DELTA Methods', fontsize=22, family='Arial', pad=20)
plt.xlabel('Methods', fontsize=20, family='Arial')
plt.ylabel('E_Dicho Score', fontsize=20, family='Arial', labelpad=20)  # Adjust label padding

# Set axis ticks
plt.xticks(fontsize=18, family='Arial')
plt.yticks(fontsize=18, family='Arial')

# Set axis colors to black
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')

# Add tick lines
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.tick_params(axis='x', direction='out', length=5, width=2, colors='black')
ax.tick_params(axis='y', direction='out', length=5, width=2, colors='black')

# Remove background grid lines but keep axes
ax.grid(False)

# Save as SVG format
output_path = 'E:/Evaluate_results_for_all_datasets/Evaluate_table/E_Dicho/Comparison_scatter_E_Dicho.svg'
plt.savefig(output_path, format='svg', dpi=600)

# Show plot
plt.tight_layout()
plt.show()
