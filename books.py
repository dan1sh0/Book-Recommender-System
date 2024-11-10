import pandas as pd

# read the dataset
df = pd.read_csv('books.csv', on_bad_lines='skip')

print(df.head())
