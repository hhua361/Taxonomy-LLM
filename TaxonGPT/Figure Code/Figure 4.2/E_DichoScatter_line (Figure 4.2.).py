import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D
import numpy as np

# Load the CSV file
file_path = "E:/Evaluate_results_for_all_datasets/Evaluate_table/E_Dicho/E_Dicho_simplify.csv"
data = pd.read_csv(file_path)

# Clean and organize data by processing experiment results for each dataset
api_data = data.melt(id_vars=['Dataset/time'],
                     value_vars=['E_DichoAPI (average)'],
                     var_name='Trial', value_name='Runtime')
api_data['Method'] = 'API'

web_data = data.melt(id_vars=['Dataset/time'],
                     value_vars=['E_DichoWEB (average)'],
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

# Create a column to represent method order
method_order = {'API': 0, 'Web': 1, 'DELTA': 2}
combined_data['MethodOrder'] = combined_data['Method'].map(method_order)

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

# Create violin plot
plt.figure(figsize=(14, 8))
ax = sns.violinplot(data=combined_data, x='Method', y='Runtime', hue='Method',
                    palette=palette, inner=None, linewidth=2, legend=False)

# Remove fill colors
for collection in ax.collections:
    collection.set_facecolor('none')

# Add scatter points and connection lines for each dataset
for i, dataset in enumerate(combined_data['Dataset'].unique()):
    subset = combined_data[combined_data['Dataset'] == dataset]
    x = subset['MethodOrder'].values + np.random.uniform(-0.1, 0.1, size=len(subset))
    y = subset['Runtime'].values
    plt.plot(x, y, marker='o', markersize=15, linestyle='-', linewidth=3, alpha=0.7, color=scatter_palette[i], markeredgecolor='black')

# Create custom legend
custom_lines = [Line2D([0], [0], color=scatter_palette[i], lw=4) for i in range(len(combined_data['Dataset'].unique()))]
legend = plt.legend(custom_lines, combined_data['Dataset'].unique(), title='Dataset', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=14, title_fontsize=16)
plt.setp(legend.get_title(), family='Arial')
for text in legend.get_texts():
    text.set_family('Arial')

# Set plot title and labels
plt.title('Comparison of E_Dicho between API, Web, and DELTA Methods', fontsize=22, family='Arial', pad=20)
plt.xlabel('Methods', fontsize=20, family='Arial')
plt.ylabel('E_Dicho Score', fontsize=20, family='Arial', labelpad=20)

# Set axis ticks
plt.xticks(ticks=[0, 1, 2], labels=['API', 'Web', 'DELTA'], fontsize=18, family='Arial')
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
output_path = 'E:/Evaluate_results_for_all_datasets/Evaluate_table/E_Dicho/Comparison_violin_E_Dicho.svg'
plt.savefig(output_path, format='svg', dpi=600)

# Show plot
plt.tight_layout()
plt.show()
