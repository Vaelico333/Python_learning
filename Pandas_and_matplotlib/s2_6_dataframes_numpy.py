import pandas as pd
import numpy as np

# I create a Numpy array based on a range and give it a certain shape
new_array = np.arange(0,33).reshape(3,11)
print(new_array)

# I convert the previous array into a Pandas data frame
# and give each column a name
df = pd.DataFrame(data=new_array, columns=['A','B','C','D','E','F',
'G','H','I','J','K'])
print(df)
