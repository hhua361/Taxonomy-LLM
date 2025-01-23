import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Data Cleaning (Preserve Original Logic)
file_path = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Data-test/2.3 Description to Matrix/Description to Matrix (Simulation 3).csv"
data = pd.read_csv(file_path)
data_cleaned = data.rename(columns={'Unnamed: 0': 'Model', 'Character number': 'Character_Number'})
data_cleaned['Model'] = data_cleaned['Model'].ffill()

accuracy_columns = ['Accuracy1', 'Accuracy2', 'Accuracy3', 'Accuracy4', 'Accuracy5']
columns_to_keep = ['Model', 'Character_Number'] + accuracy_columns
data_cleaned = data_cleaned[columns_to_keep]

for col in accuracy_columns:
    data_cleaned[col] = data_cleaned[col].str.rstrip('%').astype(float) / 100.0

data_cleaned['Average_Accuracy'] = data_cleaned[accuracy_columns].mean(axis=1)
grouped_data = data_cleaned.groupby(['Model', 'Character_Number'])['Average_Accuracy'].mean().unstack()


# Step 2: Plotting Function (Correct Bar Offset on X-axis)
def plot_bar_and_line(grouped_data, line_colors, marker_colors, output_file):
    """
    Plot bar and line charts with corrected bar offsets on the X-axis.

    Parameters:
    grouped_data (DataFrame): Grouped data (Model x Character Number)
    line_colors (list): Colors for line plots
    marker_colors (list): Colors for data points
    output_file (str): Path to save the output SVG file
    """
    fig, ax = plt.subplots(figsize=(14, 4))

    x_positions = np.arange(len(grouped_data.columns))  # Positions for character numbers
    bar_width = 0.5  # Adjust bar width (suitable for multiple models)
    total_width = bar_width * len(grouped_data.index)  # Total width of all bars

    # Adjust bar starting positions for centered distribution
    for i, model in enumerate(grouped_data.index):
        offset = (i - len(grouped_data.index) / 2) * bar_width + bar_width / 2  # Center offset
        ax.bar(
            x_positions + offset,  # Adjust starting positions for each group of bars
            grouped_data.loc[model],
            width=bar_width,
            label=f'{model} (Bar)',
            color=['#C0DAF2'][i % 3]  # Dynamically assign colors
        )

        # Add line plots
        ax.plot(
            x_positions + offset,  # Align X-axis positions with bars
            grouped_data.loc[model],
            marker='o',
            markersize=8,
            markerfacecolor=marker_colors[i % len(marker_colors)],
            markeredgecolor='black',
            markeredgewidth=1,
            label=f'{model} (Line)',
            color=line_colors[i % len(line_colors)],
            linestyle='--',
            linewidth=2
        )

    # Set X-axis labels, title, and ticks
    ax.set_xlabel('Character Numbers', fontsize=12)
    ax.set_ylabel('Average Similarity', fontsize=12)
    ax.set_title('Average Similarity of Simulation 1 by Character Numbers', fontsize=14, pad=20)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(grouped_data.columns, rotation=45, ha='right', fontsize=10)

    # Adjust legend position and layout
    ax.legend(
        title='Character Numbers',
        fontsize=8,
        title_fontsize=10,
        loc='center left',
        bbox_to_anchor=(1.01, 0.5),
        ncol=1
    )

    # Add gridlines
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Adjust layout to accommodate the legend
    plt.tight_layout(rect=[0, 0, 0.85, 1])

    # Save the figure as an SVG file
    plt.savefig(output_file, format='png', dpi=600)
    print(f"Figure saved to: {output_file}")


# Step 3: Set Colors and Plot the Image
line_colors = ['#F0AFA8']  # Line colors
marker_colors = ['#EF7A6D']  # Marker colors
output_file = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Figure-Chapter 2/SVG/Figure 2.7.png"

# Call the plotting function
plot_bar_and_line(grouped_data, line_colors, marker_colors, output_file)
