import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
iiit_dharwad_data = all_rounds[all_rounds['Institute'] == 'Indian Institute of Information Technology Dharwad']

# Convert 'Opening Rank' and 'Closing Rank' to numeric, coercing errors to NaN
iiit_dharwad_data['Opening Rank'] = pd.to_numeric(iiit_dharwad_data['Opening Rank'], errors='coerce')
iiit_dharwad_data['Closing Rank'] = pd.to_numeric(iiit_dharwad_data['Closing Rank'], errors='coerce')

# Plot number of seats based on gender-neutral and female-only categories
gender_seats = iiit_dharwad_data.groupby('Seat Pool')['Quota'].count().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=gender_seats, x='Seat Pool', y='Quota', palette='viridis')
plt.title('Number of Seats Based on Gender-Neutral and Female-Only Categories')
plt.xlabel('Seat Pool')
plt.ylabel('Number of Seats')
plt.savefig('/Users/arnavangarkar/Downloads/iiit_dharwad_gender_seats.png')
plt.show()

# Plot number of seats based on seat type
seat_type_seats = iiit_dharwad_data.groupby('Seat Type')['Quota'].count().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=seat_type_seats, x='Seat Type', y='Quota', palette='viridis')
plt.title('Number of Seats Based on Seat Type')
plt.xlabel('Seat Type')
plt.ylabel('Number of Seats')
plt.xticks(rotation=45)
plt.savefig('/Users/arnavangarkar/Downloads/iiit_dharwad_seat_type_seats.png')
plt.show()

# Plot opening and closing ranks for all three branches
plt.figure(figsize=(10, 6))
sns.lineplot(data=iiit_dharwad_data, x='Academic Program Name', y='Opening Rank', hue='Seat Type', marker='o')
sns.lineplot(data=iiit_dharwad_data, x='Academic Program Name', y='Closing Rank', hue='Seat Type', marker='x')
plt.title('Opening and Closing Ranks for All Branches at IIIT Dharwad')
plt.xlabel('Academic Program Name')
plt.ylabel('Rank')
plt.xticks(rotation=45)
plt.legend(title='Seat Type')
plt.savefig('/Users/arnavangarkar/Downloads/iiit_dharwad_opening_closing_ranks.png')
plt.show()