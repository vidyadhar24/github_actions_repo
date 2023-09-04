import pandas as pd

# Read the CSV file
df = pd.read_csv('countries.csv')
print("reading from the csv completed")

# Calculate per capita income and add it as a new column
df['Per Capita Income'] = df['GDP (in billions)'] * 1e9 / df['Population']

# Set the threshold for per capita income (you can change this value)
threshold = 10000  # Change this value to your desired threshold

# Filter countries by per capita income
filtered_df = df[df['Per Capita Income'] > threshold]

# Save the filtered data as another CSV file
filtered_df.to_csv('filtered_countries.csv', index=False)

print("Filtered countries saved to 'filtered_countries.csv'")
