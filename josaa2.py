import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Check for missing values
missing_values = seat_matrix.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

# Unique values in key columns
unique_institutes = seat_matrix['Institute Name'].nunique()
unique_programs = seat_matrix['Program Name'].nunique()
unique_seat_pools = seat_matrix['Seat Pool'].unique()
print(f"\nNumber of Unique Institutes: {unique_institutes}")
print(f"Number of Unique Programs: {unique_programs}")
print(f"Unique Seat Pools: {unique_seat_pools}")

# Distribution of seats
plt.figure(figsize=(12, 8))
sns.histplot(seat_matrix['Total'], bins=30, kde=True)
plt.title('Distribution of Total Seats')
plt.xlabel('Total Seats')
plt.ylabel('Frequency')
plt.savefig('/Users/arnavangarkar/Downloads/total_seats_distribution.png')
plt.close()

# Outliers in seat allocation
plt.figure(figsize=(12, 8))
sns.boxplot(data=seat_matrix, y='Total')
plt.title('Box Plot of Total Seats')
plt.ylabel('Total Seats')
plt.savefig('/Users/arnavangarkar/Downloads/total_seats_boxplot.png')
plt.close()

# Correlation analysis
correlation_matrix = seat_matrix[['OPEN', 'OPEN-PwD', 'GEN-EWS', 'GEN-EWS-PwD', 'SC', 'SC-PwD', 'ST', 'ST-PwD', 'OBC-NCL', 'OBC-NCL-PwD', 'Total']].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.savefig('/Users/arnavangarkar/Downloads/correlation_matrix_heatmap.png')
plt.close()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Check for missing values
missing_values = seat_matrix.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

# Unique values in key columns
unique_institutes = seat_matrix['Institute Name'].nunique()
unique_programs = seat_matrix['Program Name'].nunique()
unique_seat_pools = seat_matrix['Seat Pool'].unique()
print(f"\nNumber of Unique Institutes: {unique_institutes}")
print(f"Number of Unique Programs: {unique_programs}")
print(f"Unique Seat Pools: {unique_seat_pools}")

# Distribution of seats
plt.figure(figsize=(12, 8))
sns.histplot(seat_matrix['Total'], bins=30, kde=True)
plt.title('Distribution of Total Seats')
plt.xlabel('Total Seats')
plt.ylabel('Frequency')
plt.savefig('/Users/arnavangarkar/Downloads/total_seats_distribution.png')
plt.close()

# Outliers in seat allocation
plt.figure(figsize=(12, 8))
sns.boxplot(data=seat_matrix, y='Total')
plt.title('Box Plot of Total Seats')
plt.ylabel('Total Seats')
plt.savefig('/Users/arnavangarkar/Downloads/total_seats_boxplot.png')
plt.close()

# Correlation analysis
correlation_matrix = seat_matrix[['OPEN', 'OPEN-PwD', 'GEN-EWS', 'GEN-EWS-PwD', 'SC', 'SC-PwD', 'ST', 'ST-PwD', 'OBC-NCL', 'OBC-NCL-PwD', 'Total']].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.savefig('/Users/arnavangarkar/Downloads/correlation_matrix_heatmap.png')
plt.close()

# Programs with 0 seats
zero_seat_programs = seat_matrix[seat_matrix['Total'] == 0]
zero_seat_programs_count = zero_seat_programs.groupby(['Program Name', 'Seat Pool']).size().reset_index(name='Count')

# Print the results
print("\nPrograms with 0 Seats:")
print(zero_seat_programs_count)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Check for missing values
missing_values = seat_matrix.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

# Unique values in key columns
unique_institutes = seat_matrix['Institute Name'].nunique()
unique_programs = seat_matrix['Program Name'].nunique()
unique_seat_pools = seat_matrix['Seat Pool'].unique()
print(f"\nNumber of Unique Institutes: {unique_institutes}")
print(f"Number of Unique Programs: {unique_programs}")
print(f"Unique Seat Pools: {unique_seat_pools}")

# Distribution of seats
plt.figure(figsize=(12, 8))
sns.histplot(seat_matrix['Total'], bins=30, kde=True)
plt.title('Distribution of Total Seats')
plt.xlabel('Total Seats')
plt.ylabel('Frequency')
plt.savefig('/Users/arnavangarkar/Downloads/total_seats_distribution.png')
plt.close()

# Outliers in seat allocation
plt.figure(figsize=(12, 8))
sns.boxplot(data=seat_matrix, y='Total')
plt.title('Box Plot of Total Seats')
plt.ylabel('Total Seats')
plt.savefig('/Users/arnavangarkar/Downloads/total_seats_boxplot.png')
plt.close()

# Correlation analysis
correlation_matrix = seat_matrix[['OPEN', 'OPEN-PwD', 'GEN-EWS', 'GEN-EWS-PwD', 'SC', 'SC-PwD', 'ST', 'ST-PwD', 'OBC-NCL', 'OBC-NCL-PwD', 'Total']].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.savefig('/Users/arnavangarkar/Downloads/correlation_matrix_heatmap.png')
plt.close()

# Programs with 0 seats
zero_seat_programs = seat_matrix[seat_matrix['Total'] == 0]
zero_seat_programs_count = zero_seat_programs.groupby(['Program Name', 'Seat Pool']).size().reset_index(name='Count')

# Print the results
print("\nPrograms with 0 Seats:")
print(zero_seat_programs_count) 