import pandas as pd
import os

try:
    df = pd.read_csv('./chatgpt/best_selling_artists.csv')
except FileNotFoundError:
    print('File does not exist')

# Print the names of all the columns
print(df.columns)

df = df.sort_values(by='Year', ascending=False)

# Print the first 10 rows of the DataFrame
print(df.head(10))

for i in range(10):
    # Check if the index or key exists in the DataFrame
    if i in df.index:
        # Access the element using the correct label
        element = df.loc[i]
        # Do something with the element
        print(element)
    else:
        print(f'Index {i} does not exist')
