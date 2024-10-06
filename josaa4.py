import pandas as pd
import matplotlib.pyplot as plt

# Load the seat matrix data
seat_matrix_file = '/Users/arnavangarkar/Downloads/2024_Seat_Matrix.csv'
seat_matrix = pd.read_csv(seat_matrix_file)

# Filter the data for IIT Dharwad
iit_dharwad_data = seat_matrix[seat_matrix['Institute Name'] == 'Indian Institute of Technology Dharwad']

# Initialize a dictionary to store the results
ratios = {
    'Seat Type': [],
    'Gender-Neutral Seats': [],
    'Female-only Seats': [],
    'Ratio (Female-only / Gender-Neutral)': []
}
 
# List of seat types to calculate ratios for
seat_types = ['OPEN', 'OPEN-PwD', 'GEN-EWS', 'GEN-EWS-PwD', 'SC', 'SC-PwD', 'ST', 'ST-PwD', 'OBC-NCL', 'OBC-NCL-PwD']

# Calculate the ratios for each seat type
for seat_type in seat_types:
    gender_neutral_seats = iit_dharwad_data[iit_dharwad_data['Seat Pool'] == 'Gender-Neutral'][seat_type].sum()
    female_only_seats = iit_dharwad_data[iit_dharwad_data['Seat Pool'] == 'Female-only (including Supernumerary)'][seat_type].sum()
    
    if gender_neutral_seats > 0:
        ratio = female_only_seats / gender_neutral_seats
    else:
        ratio = None  # Avoid division by zero
    
    ratios['Seat Type'].append(seat_type)
    ratios['Gender-Neutral Seats'].append(gender_neutral_seats)
    ratios['Female-only Seats'].append(female_only_seats)
    ratios['Ratio (Female-only / Gender-Neutral)'].append(ratio)

# Convert the results to a DataFrame
ratios_df = pd.DataFrame(ratios)

# Print the results
print(ratios_df)

# Plot the ratios
plt.figure(figsize=(12, 8))
plt.bar(ratios_df['Seat Type'], ratios_df['Ratio (Female-only / Gender-Neutral)'], color='skyblue')
plt.title('Ratio of Female-only to Gender-Neutral Seats for Each Seat Type at IIT Dharwad')
plt.xlabel('Seat Type')
plt.ylabel('Ratio (Female-only / Gender-Neutral)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/Users/arnavangarkar/Downloads/gender_ratio_iit_dharwad.png')
plt.show()


