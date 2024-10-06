import pandas as pd

# Load the seat matrix data
seat_matrix_file = '/Users/arnavangarkar/Downloads/2024_Seat_Matrix.csv'
seat_matrix = pd.read_csv(seat_matrix_file)

# Filter the data for IIITs and NITs
iiit_data = seat_matrix[seat_matrix['Institute Name'].str.contains('Indian Institute of Information Technology')]
nit_data = seat_matrix[seat_matrix['Institute Name'].str.contains('National Institute of Technology')]

# Filter for gender-neutral seat pool
iiit_gender_neutral = iiit_data[iiit_data['Seat Pool'] == 'Gender-Neutral']
nit_gender_neutral = nit_data[nit_data['Seat Pool'] == 'Gender-Neutral']

# Calculate the total number of seats for gender-neutral categories
total_iiit_gender_neutral_seats = iiit_gender_neutral['Total'].sum()
total_nit_gender_neutral_seats = nit_gender_neutral['Total'].sum()

# Print the results
print(f"Total number of gender-neutral seats in IIITs: {total_iiit_gender_neutral_seats}")
print(f"Total number of gender-neutral seats in NITs: {total_nit_gender_neutral_seats}")