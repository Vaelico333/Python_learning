import pandas as pd
df=pd.read_csv('E:/Curso_Analisis_Datos/github/sample_data/02 Introduction to Pandas/intel.csv')

# We create a series using the column Open, and the check its type
open = df['Open']
print(type(open))

# By asking for its values, we see it's a Numpy array
new_open = open.values
print(type(new_open))

# Finally, we print the array to see what it looks like
print(new_open)
