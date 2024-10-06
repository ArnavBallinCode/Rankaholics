import pandas as pd

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

# Filter the data for IIT Dharwad and SC category
iit_dharwad_sc_data = all_rounds[(all_rounds['Institute'] == 'Indian Institute of Information Technology(IIIT) Dharwad') & (all_rounds['Seat Type'] == 'SC')]

# Convert 'Closing Rank' to numeric, coercing errors to NaN
iit_dharwad_sc_data['Closing Rank'] = pd.to_numeric(iit_dharwad_sc_data['Closing Rank'], errors='coerce')

# Calculate the average cutoff rank
average_cutoff_rank = iit_dharwad_sc_data['Closing Rank'].mean()

# Print the result
print(f"Average cutoff rank for the SC category at Indian Institute of Technology Dharwad: {average_cutoff_rank}")