import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
file_path_1 = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Data-test/2.3 Description to Matrix/Description to Matrix (Simulation 1).csv"
file_path_2 = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Data-test/2.3 Description to Matrix/Description to Matrix (Simulation 1 compare).csv"

data_1 = pd.read_csv(file_path_1)
data_2 = pd.read_csv(file_path_2)

# Process dataset 1
character_numbers_1 = data_1['Character number']
accuracy_columns_1 = [col for col in data_1.columns if col.startswith('Accuracy')]
accuracy_values_1 = data_1[accuracy_columns_1].apply(lambda x: x.str.rstrip('%').astype(float) / 100.0, axis=0)
mean_accuracy_1 = accuracy_values_1.mean(axis=1)
std_deviation_1 = accuracy_values_1.std(axis=1)

# Process dataset 2
character_numbers_2 = data_2['Character number']
accuracy_api = data_2['Accuracy (API)'].str.rstrip('%').astype(float) / 100.0
accuracy_web = data_2['Accuracy (Web)'].str.rstrip('%').astype(float) / 100.0

# Define styles for the plots
styles = {
    'Simulation 1': {
        'line_color': '#EF7A6D',
        'point_color': '#4B96DD',
        'scatter_color': '#F0AFA8',
        'error_bar_color': '#4B96DD'
    },
    'Comparison': {
        'api_line_color': '#9DC3E7',
        'api_point_color': '#4B96DD',
        'web_line_color': '#EF7A6D',
        'web_point_color': '#EB402D',
        'difference_line_color': 'gray'
    }
}

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 4))

# Plot Simulation 1
axes[0].plot(
    character_numbers_1, mean_accuracy_1, color=styles['Simulation 1']['line_color'],
    linestyle='-', label='Trend Line', zorder=1
)
axes[0].errorbar(
    character_numbers_1, mean_accuracy_1, yerr=std_deviation_1, fmt='o',
    color=styles['Simulation 1']['point_color'], ecolor=styles['Simulation 1']['error_bar_color'],
    elinewidth=1, capsize=5, label='Mean Accuracy ± Standard Deviation', zorder=2
)
for col in accuracy_columns_1:
    axes[0].scatter(
        character_numbers_1, accuracy_values_1[col],
        color=styles['Simulation 1']['scatter_color'], alpha=0.5, s=20, zorder=0
    )
axes[0].set_title('Accuracy of the classification task in Simulation 2', fontsize=14, pad=20)
axes[0].set_xlabel('Character Number', fontsize=12)
axes[0].set_ylabel('Accuracy (%)', fontsize=12)
axes[0].legend(fontsize=10)
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].text(-0.15, 1.05, 'A', transform=axes[0].transAxes, fontsize=16, fontweight='bold', va='top')

# Plot Comparison
axes[1].plot(
    character_numbers_2, accuracy_api, color=styles['Comparison']['api_line_color'],
    linestyle='-', marker='o', label='API: Accuracy', zorder=1
)
axes[1].scatter(
    character_numbers_2, accuracy_api, color=styles['Comparison']['api_point_color'], label='API: Mean Points', zorder=2
)
axes[1].plot(
    character_numbers_2, accuracy_web, color=styles['Comparison']['web_line_color'],
    linestyle='-', marker='o', label='Web: Accuracy', zorder=1
)
axes[1].scatter(
    character_numbers_2, accuracy_web, color=styles['Comparison']['web_point_color'], label='Web: Mean Points', zorder=2
)
# Add differences and labels
for x, y1, y2 in zip(character_numbers_2, accuracy_api, accuracy_web):
    axes[1].plot(
        [x, x], [y1, y2], linestyle='--', color=styles['Comparison']['difference_line_color'], alpha=0.7, linewidth=1
    )
    diff = abs(y1 - y2)  # Calculate the absolute difference
    axes[1].text(
        x, (y1 + y2) / 2, f'{diff:.2%}', color='black', fontsize=10, ha='center', va='center',
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, boxstyle='round,pad=0.3')
    )

axes[1].set_title('Accuracy Comparison Between API and Web Datasets', fontsize=14, pad=20)
axes[1].set_xlabel('Character Number', fontsize=12)
axes[1].set_ylabel('Accuracy (%)', fontsize=12)
axes[1].legend(fontsize=10)
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].text(-0.15, 1.05, 'B', transform=axes[1].transAxes, fontsize=16, fontweight='bold', va='top')

# Adjust layout and display
plt.tight_layout()
plt.savefig("D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Figure-Chapter 2/SVG/Figure 2.5.png", format='png', dpi=600)
plt.show()
