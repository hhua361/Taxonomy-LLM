import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the CSV file
file_path = "E:/Evaluate_results_for_all_datasets/Evaluate_table/Description/runtime/Running time average.csv"
data = pd.read_csv(file_path)

# Clean and organize data by processing results from 5 experiments for each dataset
api_data = data.melt(id_vars=['dataset/time'],
                     value_vars=['API time1', 'API time2', 'API time3', 'API time4', 'API time5'],
                     var_name='Trial', value_name='Runtime')
api_data['Method'] = 'API'

web_data = data.melt(id_vars=['dataset/time'],
                     value_vars=['WEB time1', 'WEB time2', 'WEB time3', 'WEB time4', 'WEB time5'],
                     var_name='Trial', value_name='Runtime')
web_data['Method'] = 'Web'

# Combine API and Web data
combined_data = pd.concat([api_data, web_data])

# Rename columns
combined_data.rename(columns={'dataset/time': 'Dataset'}, inplace=True)

# Set font to Arial
plt.rcParams["font.family"] = "Arial"

# Set style
sns.set(style="whitegrid")

# Define colors
api_color = '#EF7A6D'  # Light red
web_color = '#9DC3E7'  # Light blue

palette = [
    '#FF9999', '#FFB3B3', '#FFD9D9', '#FFE5E5',  # Light red shades
    '#2E75B6',  # Darker blue
    '#9DC3E7', '#AED8F0', '#ADD8E6', '#BFECF9', '#D0F0FF', '#E0F7FF'  # Light blue shades
]

# Create boxplots and scatterplots
plt.figure(figsize=(14, 8))

# Draw boxplots for API and Web methods
ax = sns.boxplot(data=combined_data, x='Method', y='Runtime', hue='Method',
                 showfliers=False, width=0.6, linewidth=1.7,
                 boxprops=dict(facecolor='none', edgecolor='black'),
                 medianprops=dict(color='black'))

# Draw scatterplot
sns.stripplot(data=combined_data, x='Method', y='Runtime', hue='Dataset',
              dodge=True, jitter=0.2, marker='o', palette=palette, alpha=1, linewidth=1, s=15)

# Annotate medians
medians = combined_data.groupby(['Method'])['Runtime'].median().values
for i, median in enumerate(medians):
    ax.text(i, median + 2, f'{int(median)}', ha='center', va='bottom', fontweight='bold', color='grey', fontsize=12, family='Arial')

# Adjust legend
legend = plt.legend(title='Dataset', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=14, title_fontsize=16)
plt.setp(legend.get_title(), family='Arial')
for text in legend.get_texts():
    text.set_family('Arial')

# Set plot title and labels
plt.title('Comparison of Taxonomic Key Runtime between API and Web Methods', fontsize=22, family='Arial', pad=20)
plt.xlabel('Methods', fontsize=20, family='Arial')
plt.ylabel('Runtime (seconds)', fontsize=20, family='Arial', labelpad=20)

# Set axis ticks and styles
plt.xticks(fontsize=18, family='Arial')
plt.yticks(fontsize=18, family='Arial')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')
ax.tick_params(axis='x', colors='black', labelsize=18)
ax.tick_params(axis='y', colors='black', labelsize=18)

# Add tick lines
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.tick_params(axis='x', direction='out', length=5, width=2, colors='black')
ax.tick_params(axis='y', direction='out', length=5, width=2, colors='black')

# Remove background grid lines but keep axes
ax.grid(False)

plt.tight_layout()

# Save as SVG format
output_path = 'E:/Evaluate_results_for_all_datasets/Evaluate_table/Description/runtime/Running_time.svg'
plt.savefig(output_path, format='svg', dpi=600)

# Show plot
plt.show()
