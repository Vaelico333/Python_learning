import pandas as pd
df=pd.read_csv('E:/Curso_Analisis_Datos/github/sample_data/02 Introduction to Pandas/intel.csv')

# Creating a simple filter that returns a boolean
closing_price = df['Close'] > 46.0
print(closing_price)

# This filter excludes anything that the variable closing_price returns as False
print(df[closing_price])

# This filter is the simplest version of the previous
print(df[df['Open'] > 55.0])
