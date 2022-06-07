import pandas as pd
df=pd.read_csv('E:/Curso_Analisis_Datos/github/sample_data/02 Introduction to Pandas/intel.csv')
'''print(df)
print(type(df))
print(df.shape)
print(df.columns)
print(df.head(3))
print(df.tail(7))
print(df.info())
open = df['Open']
print(open.head(3))
print(df[['High','Open','Close']])
print(df.describe())'''

# Print the entire DataFrame
# print(df)

# What is the data type?
# print(type(df))

# What is the shape of our DataFrame? (rows, columns)
# print(df.shape)

# Show column names
# print(df.columns)

# Show top rows of DataFrame
# print(df.head())

# Show info summary of DataFrame
# print(df.info())

# Print a column series
# open = df['Open']
# print(open)

# Print columns side by side
# print(df[['Open','Close']].head(3))

# Show description summary of DataFrame
# print(df.describe())

# Using min with DataFrames
# print(df['Open'].min())

# Show mean open value
# print(df['Open'].mean())
