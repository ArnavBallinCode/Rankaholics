import pandas as pd

# Load the seat matrix data
seat_matrix_file = '/Users/arnavangarkar/Downloads/2024_Seat_Matrix.csv'
seat_matrix = pd.read_csv(seat_matrix_file)

# Filter the data for 'Gender-Neutral' and 'Female-only (including Supernumerary)' categories
gender_neutral = seat_matrix[seat_matrix['Seat Pool'] == 'Gender-Neutral']
female_only = seat_matrix[seat_matrix['Seat Pool'] == 'Female-only (including Supernumerary)']

# Sum the 'OPEN' seats for each category
gender_neutral_open_seats = gender_neutral['OPEN'].sum()
female_only_open_seats = female_only['OPEN'].sum()

# Calculate the ratio
ratio = female_only_open_seats / gender_neutral_open_seats

# Print the results
print(f"Total OPEN seats for Gender-Neutral: {gender_neutral_open_seats}")
print(f"Total OPEN seats for Female-only (including Supernumerary): {female_only_open_seats}")
print(f"Ratio of Female-only (including Supernumerary) to Gender-Neutral: {ratio:.2f}")