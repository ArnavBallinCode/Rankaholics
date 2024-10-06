import pandas as pd

# Load the seat matrix data
seat_matrix_file = '/Users/arnavangarkar/Downloads/2024_Seat_Matrix.csv'
seat_matrix = pd.read_csv(seat_matrix_file)

# Filter the data for IIT Dharwad
iit_dharwad_data = seat_matrix[seat_matrix['Institute Name'] == 'Indian Institute of Information Technology(IIIT) Dharwad']

# Initialize an empty list to store the results
gender_ratios = []

# Iterate over each unique program
for program in iit_dharwad_data['Program Name'].unique():
    program_data = iit_dharwad_data[iit_dharwad_data['Program Name'] == program]
    
    # Sum the seats for Gender-Neutral and Female-only (including Supernumerary)
    gender_neutral_seats = program_data[program_data['Seat Pool'] == 'Gender-Neutral']['Total'].sum()
    female_only_seats = program_data[program_data['Seat Pool'] == 'Female-only (including Supernumerary)']['Total'].sum()
    
    # Calculate the ratio
    if gender_neutral_seats > 0:
        ratio = female_only_seats / gender_neutral_seats
    else:
        ratio = None  # Avoid division by zero
    
    # Append the result to the list
    gender_ratios.append({
        'Program Name': program,
        'Gender-Neutral Seats': gender_neutral_seats,
        'Female-only Seats': female_only_seats,
        'Gender Ratio (Female-only / Gender-Neutral)': ratio
    })

# Convert the results to a DataFrame
gender_ratios_df = pd.DataFrame(gender_ratios)

# Print the results
print(gender_ratios_df)

import pandas as pd

# Load the seat matrix data
seat_matrix_file = '/Users/arnavangarkar/Downloads/2024_Seat_Matrix.csv'
seat_matrix = pd.read_csv(seat_matrix_file)

# Filter the data for IIT Dharwad
iit_dharwad_data = seat_matrix[seat_matrix['Institute Name'] == 'Indian Institute of Technology Dharwad']

# Calculate the total number of seats
total_seats = iit_dharwad_data['Total'].sum()

# Print the result
print(f"Total number of seats available at Indian Institute of Technology Dharwad: {total_seats}")


import pandas as pd

# Load the seat matrix data
seat_matrix_file = '/Users/arnavangarkar/Downloads/2024_Seat_Matrix.csv'
seat_matrix = pd.read_csv(seat_matrix_file)

# Filter the data for IIIT Dharwad
iiit_dharwad_data = seat_matrix[seat_matrix['Institute Name'] == 'Indian Institute of Information Technology Dharwad']

# Group by Program Name and Seat Type, and calculate the cutoff ranks
cutoff_ranks = iiit_dharwad_data.groupby(['Program Name', 'Seat Pool']).agg({
    'OPEN': 'max',
    'OPEN-PwD': 'max',
    'GEN-EWS': 'max',
    'GEN-EWS-PwD': 'max',
    'SC': 'max',
    'SC-PwD': 'max',
    'ST': 'max',
    'ST-PwD': 'max',
    'OBC-NCL': 'max',
    'OBC-NCL-PwD': 'max'
}).reset_index()

# Print the results
print(cutoff_ranks)