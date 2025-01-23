import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the CSV file
file_path = "D:/Desktop/Thesis project/Data_analysis (Include Table, Figure)/Data-test/2.2 Description to Matrix/Description to Matrix (DtoM re).csv"
data = pd.read_csv(file_path)

# Data preprocessing
# Extract columns related to matrix reproducibility and character list reproducibility
matrix_columns = ['DtoM-1', 'DtoM-2', 'DtoM-3', 'DtoM-4', 'Average']
character_columns = ['List-1', 'List-2', 'List-3', 'List-4']

# Convert percentage strings to float values
for col in matrix_columns + character_columns:
    data[col] = data[col].str.rstrip('%').astype(float)

# Set the dataset name as the index
data.set_index('Unnamed: 0', inplace=True)

# Extract matrix and character list data
matrix_data = data[matrix_columns[:-1]]  # Exclude the "Average" column
character_data = data[character_columns]

# Create a layout: 1x3 grid, all images in a single row
fig, axes = plt.subplots(1, 3, figsize=(21, 6), gridspec_kw={'width_ratios': [1, 1, 1]})

# Plot heatmap for matrix reproducibility
sns.heatmap(matrix_data, annot=True, fmt=".2f", cmap="Blues", cbar=True, ax=axes[0])
axes[0].set_title("Matrix Reproducibility Heatmap", fontsize=14, pad=20)
axes[0].set_xlabel("Tests", fontsize=12)
axes[0].set_ylabel("Datasets", fontsize=12)
axes[0].text(-0.15, 1.05, 'A', transform=axes[0].transAxes, fontsize=16, fontweight='bold', va='top')

# Plot heatmap for character list reproducibility
sns.heatmap(character_data, annot=True, fmt=".2f", cmap="Greens", cbar=True, ax=axes[1])
axes[1].set_title("Character List Reproducibility Heatmap", fontsize=14, pad=20)
axes[1].set_xlabel("Tests", fontsize=12)
axes[1].set_ylabel("")  # Remove duplicate Y-axis label
axes[1].text(-0.15, 1.05, 'B', transform=axes[1].transAxes, fontsize=16, fontweight='bold', va='top')

# Plot scatterplot showing the relationship between matrix and character list reproducibility
matrix_flat = matrix_data.values.flatten()
character_flat = character_data.values.flatten()

sns.scatterplot(x=character_flat, y=matrix_flat, ax=axes[2])
axes[2].set_title("Relationship between Character List and Matrix Reproducibility", fontsize=14, pad=20)
axes[2].set_xlabel("Character List Reproducibility (%)", fontsize=12)
axes[2].set_ylabel("Matrix Reproducibility (%)", fontsize=12)

# Add regression line and equation
reg = LinearRegression().fit(character_flat.reshape(-1, 1), matrix_flat)
x_vals = np.linspace(min(character_flat), max(character_flat), 100)
y_vals = reg.predict(x_vals.reshape(-1, 1))
axes[2].plot(x_vals, y_vals, color='red', linestyle='--', label='Trend Line')

# Calculate regression equation parameters
slope = reg.coef_[0]
intercept = reg.intercept_
correlation = np.corrcoef(character_flat, matrix_flat)[0, 1]

# Display the regression equation
equation = f"$y = {slope:.2f}x + {intercept:.2f}$\n$R = {correlation:.2f}$"
axes[2].text(min(character_flat), max(matrix_flat) * 0.8, equation, fontsize=12, color='Black')

# Adjust the legend position
axes[2].legend(loc='lower right')  # Place the legend in the bottom-right corner
axes[2].text(-0.15, 1.05, 'C', transform=axes[2].transAxes, fontsize=16, fontweight='bold', va='top')  # Add "C" label

# Adjust layout
plt.tight_layout()

# Save the figure
output_file = "D:/Desktop/Thesis project/Data_analysis (Include Table, Figure)/Figure-Chapter 2/SVG/Figure 2.11.png"
plt.savefig(output_file, format='png', dpi=600)

# Display the figure
plt.show()

# Print the save path
print(f"Figure saved to: {output_file}")