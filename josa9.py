import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the seat matrix data
seat_matrix_file = '/Users/arnavangarkar/Downloads/2024_Seat_Matrix.csv'
seat_matrix = pd.read_csv(seat_matrix_file)

# Filter the data for IIIT Dharwad
iiit_dharwad_data = seat_matrix[seat_matrix['Institute Name'] == 'Indian Institute of Information Technology Dharwad']

# Total number of seats
total_seats = iiit_dharwad_data['Total'].sum()
print(f"Total number of seats at IIIT Dharwad: {total_seats}")

# Seats by category
categories = ['OPEN', 'OPEN-PwD', 'GEN-EWS', 'GEN-EWS-PwD', 'SC', 'SC-PwD', 'ST', 'ST-PwD', 'OBC-NCL', 'OBC-NCL-PwD']
seats_by_category = iiit_dharwad_data[categories].sum().reset_index()
seats_by_category.columns = ['Category', 'Seats']
print("\nSeats by Category:")
print(seats_by_category)

# Seats by gender
seats_by_gender = iiit_dharwad_data.groupby('Seat Pool')['Total'].sum().reset_index()
print("\nSeats by Gender:")
print(seats_by_gender)

# Load the round data
round_1_file = '/Users/arnavangarkar/Downloads/2024_Round_1.csv'
round_2_file = '/Users/arnavangarkar/Downloads/2024_Round_2.csv'
round_3_file = '/Users/arnavangarkar/Downloads/2024_Round_3.csv'
round_4_file = '/Users/arnavangarkar/Downloads/2024_Round_4.csv'
round_5_file = '/Users/arnavangarkar/Downloads/2024_Round_5.csv'

round_1 = pd.read_csv(round_1_file)
round_2 = pd.read_csv(round_2_file)
round_3 = pd.read_csv(round_3_file)
round_4 = pd.read_csv(round_4_file)
round_5 = pd.read_csv(round_5_file)

# Combine all rounds into a single DataFrame
all_rounds = pd.concat([round_1, round_2, round_3, round_4, round_5], ignore_index=True)

# Filter the data for IIIT Dharwad
iiit_dharwad_rounds = all_rounds[all_rounds['Institute'] == 'Indian Institute of Information Technology Dharwad']

# Convert 'Opening Rank' and 'Closing Rank' to numeric, coercing errors to NaN
iiit_dharwad_rounds['Opening Rank'] = pd.to_numeric(iiit_dharwad_rounds['Opening Rank'], errors='coerce')
iiit_dharwad_rounds['Closing Rank'] = pd.to_numeric(iiit_dharwad_rounds['Closing Rank'], errors='coerce')

# Opening and closing ranks
opening_ranks = iiit_dharwad_rounds.groupby('Seat Type')['Opening Rank'].mean().reset_index()
closing_ranks = iiit_dharwad_rounds.groupby('Seat Type')['Closing Rank'].mean().reset_index()
print("\nAverage Opening Ranks by Seat Type:")
print(opening_ranks)
print("\nAverage Closing Ranks by Seat Type:")
print(closing_ranks)

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=seats_by_category, x='Category', y='Seats', palette='viridis')
plt.title('Seats by Category at IIIT Dharwad')
plt.xlabel('Category')
plt.ylabel('Number of Seats')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/Users/arnavangarkar/Downloads/iiit_dharwad_seats_by_category.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=seats_by_gender, x='Seat Pool', y='Total', palette='viridis')
plt.title('Seats by Gender at IIIT Dharwad')
plt.xlabel('Seat Pool')
plt.ylabel('Number of Seats')
plt.tight_layout()
plt.savefig('/Users/arnavangarkar/Downloads/iiit_dharwad_seats_by_gender.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=opening_ranks, x='Seat Type', y='Opening Rank', palette='viridis')
plt.title('Average Opening Ranks by Seat Type at IIIT Dharwad')
plt.xlabel('Seat Type')
plt.ylabel('Average Opening Rank')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/Users/arnavangarkar/Downloads/iiit_dharwad_opening_ranks.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=closing_ranks, x='Seat Type', y='Closing Rank', palette='viridis')
plt.title('Average Closing Ranks by Seat Type at IIIT Dharwad')
plt.xlabel('Seat Type')
plt.ylabel('Average Closing Rank')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/Users/arnavangarkar/Downloads/iiit_dharwad_closing_ranks.png')
plt.show()