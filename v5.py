import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Hardcoded file paths
round_1_file = '/Users/arnavangarkar/Downloads/2024_Round_1.csv'
round_2_file = '/Users/arnavangarkar/Downloads/2024_Round_2.csv'
round_3_file = '/Users/arnavangarkar/Downloads/2024_Round_3.csv'
round_4_file = '/Users/arnavangarkar/Downloads/2024_Round_4.csv'
round_5_file = '/Users/arnavangarkar/Downloads/2024_Round_5.csv'
seat_matrix_file = '/Users/arnavangarkar/Downloads/2024_Seat_Matrix.csv'

# Load the data
round_1 = pd.read_csv(round_1_file)
round_2 = pd.read_csv(round_2_file)
round_3 = pd.read_csv(round_3_file)
round_4 = pd.read_csv(round_4_file)
round_5 = pd.read_csv(round_5_file)
seat_matrix = pd.read_csv(seat_matrix_file)

# Add 'Round' column to each DataFrame
round_1['Round'] = 1
round_2['Round'] = 2
round_3['Round'] = 3
round_4['Round'] = 4
round_5['Round'] = 5

# Display the first few rows of each DataFrame
print("Round 1 Data:")
print(round_1.head())
print("\nSeat Matrix Data:")
print(seat_matrix.head())

# Print column names to verify the presence of 'Institute' column
print("\nRound 1 Columns:", round_1.columns)
print("Seat Matrix Columns:", seat_matrix.columns)

# Rename columns to match
seat_matrix.rename(columns={'Institute Name': 'Institute'}, inplace=True)

# Merge round data with seat matrix data
merged_data = pd.concat([round_1, round_2, round_3, round_4, round_5], ignore_index=True)

# Ensure the 'Institute' column exists in both DataFrames
if 'Institute' in merged_data.columns and 'Institute' in seat_matrix.columns:
    merged_data = merged_data.merge(seat_matrix, on='Institute', how='left')
else:
    print("Error: 'Institute' column not found in one or both DataFrames.")
    print("Merged Data Columns:", merged_data.columns)
    print("Seat Matrix Columns:", seat_matrix.columns)
    exit()

# Display the first few rows of the merged DataFrame
print("\nMerged Data:")
print(merged_data.head())

# Analyze seat allocation trends
seat_allocation_trends = merged_data.groupby(['Institute', 'Round'])['Total'].sum().reset_index()

# Visualize seat allocation trends
plt.figure(figsize=(12, 8))
sns.lineplot(data=seat_allocation_trends, x='Round', y='Total', hue='Institute')
plt.title('Seat Allocation Trends by Institute')
plt.xlabel('Round')
plt.ylabel('Allocated Seats')
plt.legend(title='Institute', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('/Users/arnavangarkar/Downloads/seat_allocation_trends.png')
plt.show()

# Analyze cutoff ranks
cutoff_ranks = merged_data.groupby(['Institute', 'Round'])['Closing Rank'].mean().reset_index()

# Visualize cutoff ranks
plt.figure(figsize=(12, 8))
sns.lineplot(data=cutoff_ranks, x='Round', y='Closing Rank', hue='Institute')
plt.title('Cutoff Ranks by Institute')
plt.xlabel('Round')
plt.ylabel('Closing Rank')
plt.legend(title='Institute', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('/Users/arnavangarkar/Downloads/cutoff_ranks.png')
plt.show()

# Analyze seat availability
seat_availability = seat_matrix.groupby('Institute')['Total'].sum().reset_index()

# Visualize seat availability
plt.figure(figsize=(12, 8))
sns.barplot(data=seat_availability, x='Institute', y='Total')
plt.title('Total Seats by Institute')
plt.xlabel('Institute')
plt.ylabel('Total Seats')
plt.xticks(rotation=90)
plt.savefig('/Users/arnavangarkar/Downloads/seat_availability.png')
plt.show()