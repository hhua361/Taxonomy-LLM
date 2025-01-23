import pandas as pd
import matplotlib.pyplot as plt

# Set file path
file_path = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Data-test/2.3 Description to Matrix/Description to Matrix (DtoM efficiency).csv"

# Load CSV file
df = pd.read_csv(file_path)

# Calculate the average time for each dataset
df["DtoM_avg"] = df[["DtoM time1", "DtoM time2", "DtoM time3", "DtoM time4", "DtoM time5"]].mean(axis=1)
df["Web_avg"] = df[["Web time1", "Web time2", "Web time3", "Web time4", "Web time5"]].mean(axis=1)

# Adjusted DtoM average values (divide each point by 2)
df["DtoM_adjusted"] = df["DtoM_avg"] / 3

# Plot multi-line chart
plt.figure(figsize=(14, 7))

# Plot original DtoM and Web method lines
plt.plot(df["dataset/time"], df["DtoM_avg"], marker="o", label="Original DtoM Avg Time", color="#2D8FEB", linestyle="--")
plt.plot(df["dataset/time"], df["Web_avg"], marker="s", label="Web Avg Time", color="#EB402D", linestyle="-")

# Plot adjusted DtoM line
plt.plot(df["dataset/time"], df["DtoM_adjusted"], marker="^", label="Adjusted DtoM Avg Time (1/3)", color="#4F9E00", linestyle="-.")

# Plot gaps between original DtoM and Web
for i in range(len(df)):
    x = df["dataset/time"][i]
    y1 = df["DtoM_avg"][i]
    y2 = df["Web_avg"][i]
    plt.plot([x, x], [y1, y2], color="#2D8FEB", linestyle="dotted")  # Dotted line connecting points
    plt.text(x, (y1 + y2) / 2, f"{abs(y1 - y2):.1f}s", color="#2D8FEB", fontsize=9, ha="center")  # Annotate gap

# Plot gaps between adjusted DtoM and Web
for i in range(len(df)):
    x = df["dataset/time"][i]
    y1 = df["DtoM_adjusted"][i]
    y2 = df["Web_avg"][i]
    plt.plot([x, x], [y1, y2], color="#4F9E00", linestyle="dotted")  # Dotted line connecting points
    plt.text(x, (y1 + y2) / 2, f"{abs(y1 - y2):.1f}s", color="#4F9E00", fontsize=9, ha="center")  # Annotate gap

# Chart title and labels
plt.title("Comparison of Processing Time with Gaps Between DtoM and Web Methods", fontsize=14, pad=20)
plt.xlabel("Dataset", fontsize=12)
plt.ylabel("Processing Time (s)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.legend(title="Method")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save the figure as an SVG file
output_file = "D:/桌面/Thesis project/Data_analysis (Include Table, Figure)/Figure-Chapter 2/SVG/Figure 2.9.png"
plt.savefig(output_file, format="png", dpi=600)
print(f"Figure saved to: {output_file}")
