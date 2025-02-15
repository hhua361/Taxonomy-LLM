import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load your dataset
data = pd.read_csv("D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Data-test/2.2 Description to Matrix/Description to Matrix (DtoM efficiency).csv")

# Calculate average runtime for DtoM and Web methods
data['DtoM Average Time'] = data[['DtoM time1', 'DtoM time2', 'DtoM time3', 'DtoM time4', 'DtoM time5']].mean(axis=1)
data['Web Average Time'] = data[['Web time1', 'Web time2', 'Web time3', 'Web time4', 'Web time5']].mean(axis=1)

# Initialize subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# ---- Subplot 1: Species Number vs Runtime ----
model_dtom_species = LinearRegression()
model_web_species = LinearRegression()

# Fit models for species number
X_species = data['species number'].values.reshape(-1, 1)
y_dtom = data['DtoM Average Time'].values
y_web = data['Web Average Time'].values
model_dtom_species.fit(X_species, y_dtom)
model_web_species.fit(X_species, y_web)

species_data = pd.DataFrame({
    'Species Numbers': data['species number'],
    'DtoM': data['DtoM Average Time'],
    'Web': data['Web Average Time']
}).melt(id_vars=['Species Numbers'], value_vars=['DtoM', 'Web'], var_name='Method', value_name='Runtime')

sns.regplot(
    x='Species Numbers', y='Runtime', data=species_data[species_data['Method'] == 'DtoM'],
    ax=axes[0], scatter_kws={'color': '#D94636', 'alpha': 0.7},
    line_kws={'color': '#D94636', 'label': f'DtoM: y={model_dtom_species.coef_[0]:.2f}x+{model_dtom_species.intercept_:.2f}'}
)
sns.regplot(
    x='Species Numbers', y='Runtime', data=species_data[species_data['Method'] == 'Web'],
    ax=axes[0], scatter_kws={'color': '#3E8AD0', 'alpha': 0.7},
    line_kws={'color': '#3E8AD0', 'label': f'Web: y={model_web_species.coef_[0]:.2f}x+{model_web_species.intercept_:.2f}'}
)
axes[0].set_title('Species Number vs Runtime', fontsize=14, pad=20)
axes[0].set_xlabel('Species Number', fontsize=12)
axes[0].set_ylabel('Runtime (Seconds)', fontsize=12)
axes[0].legend(fontsize=10)

# Hide top and right spines and gridlines
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].grid(False)

# Add annotation for subplot A
axes[0].text(-0.05, 1.1, 'A', transform=axes[0].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

# ---- Subplot 2: Character Number vs Runtime ----
model_dtom_character = LinearRegression()
model_web_character = LinearRegression()

# Fit models for character number
X_character = data['character numbers'].values.reshape(-1, 1)
model_dtom_character.fit(X_character, y_dtom)
model_web_character.fit(X_character, y_web)

character_data = pd.DataFrame({
    'Character Numbers': data['character numbers'],
    'DtoM': data['DtoM Average Time'],
    'Web': data['Web Average Time']
}).melt(id_vars=['Character Numbers'], value_vars=['DtoM', 'Web'], var_name='Method', value_name='Runtime')

sns.regplot(
    x='Character Numbers', y='Runtime', data=character_data[character_data['Method'] == 'DtoM'],
    ax=axes[1], scatter_kws={'color': '#D94636', 'alpha': 0.7},
    line_kws={'color': '#D94636', 'label': f'DtoM: y={model_dtom_character.coef_[0]:.2f}x+{model_dtom_character.intercept_:.2f}'}
)
sns.regplot(
    x='Character Numbers', y='Runtime', data=character_data[character_data['Method'] == 'Web'],
    ax=axes[1], scatter_kws={'color': '#3E8AD0', 'alpha': 0.7},
    line_kws={'color': '#3E8AD0', 'label': f'Web: y={model_web_character.coef_[0]:.2f}x+{model_web_character.intercept_:.2f}'}
)
axes[1].set_title('Character Number vs Runtime', fontsize=14, pad=20)
axes[1].set_xlabel('Character Numbers', fontsize=12)
axes[1].set_ylabel('')
axes[1].legend(fontsize=10)

# Hide top and right spines and gridlines
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].grid(False)

# Add annotation for subplot B
axes[1].text(-0.05, 1.1, 'B', transform=axes[1].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

# Adjust layout and save the figure as SVG
plt.tight_layout()
output_file = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Figure-Chapter 2/SVG/Figure 2.10.png"
plt.savefig(output_file, format="png", dpi=600)
print(f"Figure saved to: {output_file}")
