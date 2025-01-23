import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np

# Set font to Arial
plt.rcParams['font.family'] = 'Arial'

# Load the user-uploaded file
file_path = "E:/Evaluate_results_for_all_datasets/Evaluate_table/Description/API fee/API fee.csv"
data_fee = pd.read_csv(file_path)

# Clean the data by converting the price column to float
data_fee['5 times money'] = data_fee['5 times money'].str.replace('$', '').astype(float)

# Create a 3D plot
fig = plt.figure(figsize=(13, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot a 3D scatter plot
scatter = ax.scatter(data_fee['species number'], data_fee['character number'], data_fee['5 times money'], c='#EF7A6D', marker='o', s=100, alpha=0.6)

# Add axis labels
ax.set_xlabel('Species Number', fontsize=18)
ax.set_ylabel('Character Number', fontsize=18)
ax.set_zlabel('API Fee (5 times) ($)', fontsize=18)

# Add title
ax.set_title('Effect of Species and Character Numbers on API Fee about Taxonomic Description', fontsize=20)

# Compute the regression plane
X = data_fee[['species number', 'character number']]
X = sm.add_constant(X)
model = sm.OLS(data_fee['5 times money'], X).fit()
x_surf, y_surf = np.meshgrid(np.linspace(X['species number'].min(), X['species number'].max(), 100),
                             np.linspace(X['character number'].min(), X['character number'].max(), 100))
z_surf = model.params[0] + model.params[1] * x_surf + model.params[2] * y_surf

# Plot the regression plane
ax.plot_surface(x_surf, y_surf, z_surf, color='#9DC3E7', alpha=0.3)

# Add the regression equation to the plot
equation_text = f'API Fee = {model.params[0]:.2f} + {model.params[1]:.2f}*Species Number + {model.params[2]:.2f}*Character Number'
ax.text2D(0.05, 0.775, equation_text, transform=ax.transAxes, fontsize=16, color='black', horizontalalignment='left', verticalalignment='top')

# Adjust the viewing angle
ax.view_init(elev=40, azim=120)

# Add legend
scatter_proxy = plt.Line2D([0], [0], linestyle="none", c='#EF7A6D', marker='o')
surface_proxy = plt.Line2D([0], [0], linestyle="none", c='#9DC3E7', marker='s', markersize=10)
ax.legend([scatter_proxy, surface_proxy], ['Data Points', 'Regression Plane'], numpoints=1, loc='upper right', fontsize=12, frameon=True, fancybox=True, framealpha=0.7)

# Save as SVG format
output_path = 'E:/Evaluate_results_for_all_datasets/Evaluate_table/Description/API fee/API_fee_taxonomic_description.svg'
plt.savefig(output_path, format='svg', dpi=600)

plt.show()