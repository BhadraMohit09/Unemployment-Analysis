import pandas as pd

# Load the datasets
file_path_1 = 'Unemployment in India.csv'
file_path_2 = 'Unemployment_Rate_upto_11_2020.csv'

data_1 = pd.read_csv(file_path_1)
data_2 = pd.read_csv(file_path_2)

# Step 1: Standardize Column Names
data_1.columns = data_1.columns.str.strip().str.lower().str.replace(' ', '_')
data_2.columns = data_2.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 2: Trim whitespace and parse dates correctly
data_1['date'] = pd.to_datetime(data_1['date'].str.strip(), format='%d-%m-%Y', errors='coerce')
data_2['date'] = pd.to_datetime(data_2['date'].str.strip(), format='%d-%m-%Y', errors='coerce')

# Check for rows with unparsed dates (NaT) and drop if necessary
data_1 = data_1.dropna(subset=['date'])
data_2 = data_2.dropna(subset=['date'])

# Step 3: Rename overlapping columns for clarity during merge
data_2 = data_2.rename(columns={'region.1': 'region_secondary'})

# Step 4: Merge Datasets on 'region' and 'date'
merged_data = pd.merge(data_1, data_2, on=['region', 'date'], how='outer', suffixes=('_data1', '_data2'))

# Step 5: Save the merged data
merged_data.to_csv('merged_unemployment_data.csv', index=False)

# Display the first few rows of the merged dataset
merged_data.head()
