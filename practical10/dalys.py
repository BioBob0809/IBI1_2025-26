import os
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# 1. Import the .csv dataset
# --------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print("Dataset imported successfully.")

# --------------------------
# 2. Show Year and DALYs for the first 10 rows
# --------------------------
# Show the third and fourth columns (index 2 and 3) for the first 10 rows
first_10_subset = dalys_data.iloc[:10, [2, 3]]
print("\nFirst 10 rows (Year and DALYs):")
print(first_10_subset)

# Afghanistan's first 10 records and the year with maximum DALYs
afghanistan_data = dalys_data[dalys_data['Entity'] == 'Afghanistan'].head(10)
max_daly_row = afghanistan_data.loc[afghanistan_data['DALYs'].idxmax()]
max_year_afghanistan = max_daly_row['Year']
# The year with the maximum DALYs across the first 10 recorded years in Afghanistan
print(f"\nThe year with the maximum DALYs in Afghanistan's first 10 records: {max_year_afghanistan}")

# --------------------------
# 3. Zimbabwe data using Boolean indexing
# --------------------------
zimbabwe_boolean = dalys_data['Entity'] == 'Zimbabwe'
zimbabwe_data = dalys_data.loc[zimbabwe_boolean]
zimbabwe_years = zimbabwe_data['Year'].tolist()
first_year_zimbabwe = min(zimbabwe_years)
last_year_zimbabwe = max(zimbabwe_years)
print(f"\nAll years with recorded DALYs in Zimbabwe: {zimbabwe_years}")
# The first recorded year for Zimbabwe DALYs data
print(f"First recorded year for Zimbabwe: {first_year_zimbabwe}")
# The last recorded year for Zimbabwe DALYs data
print(f"Last recorded year for Zimbabwe: {last_year_zimbabwe}")

# --------------------------
# 4. Countries with max and min DALYs in 2019
# --------------------------
data_2019 = dalys_data[dalys_data['Year'] == 2019]
max_daly_2019 = data_2019.loc[data_2019['DALYs'].idxmax()]
min_daly_2019 = data_2019.loc[data_2019['DALYs'].idxmin()]
max_country = max_daly_2019['Entity']
min_country = min_daly_2019['Entity']
# Country with maximum DALYs in 2019
print(f"\nCountry with maximum DALYs in 2019: {max_country}")
# Country with minimum DALYs in 2019
print(f"Country with minimum DALYs in 2019: {min_country}")

# --------------------------
# 5. Plot DALYs over time for one country
# --------------------------
plot_data = dalys_data[dalys_data['Entity'] == max_country]
plt.figure(figsize=(10, 6))
plt.plot(plot_data['Year'], plot_data['DALYs'], marker='o', linestyle='-', color='blue')
plt.title(f'DALYs Over Time in {max_country}')
plt.xlabel('Year')
plt.ylabel('DALYs (Disability-Adjusted Life Years)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Save plot to 'plots' folder
output_folder = "plots"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
plt.savefig(f"{output_folder}/{max_country}_dalys_trend.png", dpi=300)
print(f"\nPlot saved to: {output_folder}/{max_country}_dalys_trend.png")

# --------------------------
# 6. Answer the question from question.txt
# --------------------------
def answer_question():
    try:
        with open("question.txt", "r") as f:
            question = f.read().strip()
        print(f"\nQuestion from question.txt: {question}")

        # Example analysis (customize based on your actual question)
        # This example answers: "What was the average DALYs value in 2019?"
        avg_dalys_2019 = data_2019['DALYs'].mean()
        print(f"Answer: The average DALYs value across all countries in 2019 was {avg_dalys_2019:.2f}.")
    except FileNotFoundError:
        print("\nWarning: question.txt not found. Please add the file with your question.")

answer_question()