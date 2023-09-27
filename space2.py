import pandas as pd
import io

# Specify the file path
URL = r'C:\Users\borch\Desktop\dataset_part_1.csv'  # You should provide the full path to your CSV file

# Read the CSV file using pandas
df = pd.read_csv(URL)

# Display the first 10 rows of the DataFrame
print(df.head(10))

# Calculate the percentage of missing values for each column
missing_percentages = (df.isnull().sum() / df.shape[0]) * 100
print("Percentage of missing values:")
print(missing_percentages)

# Display the data types of columns
print("Data types of columns:")
print(df.dtypes)

# Print the result of the 'all' method, which checks if all values in each column are True
print("Result of df.all():")
print(df.all())
print(df.LaunchSite.value_counts())
print(df.Orbit.value_counts())
landing_outcomes = {}
landing_outcomes = df.Outcome.value_counts()
print(landing_outcomes)
for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)
bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
print(bad_outcomes)
landing_pad = []
j = 0
for i in df.Outcome : 
    if i in bad_outcomes :
        j += 1
        continue
    else :
        landing_pad.append(i)
        df.i = 1

print(j)
