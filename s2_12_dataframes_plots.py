import pandas as pd
import matplotlib.pyplot as plt

# I read the file and tell python to use the column 'Date' as index, and that it will be a datetime object
df = pd.read_csv('../../sample_data/02 Introduction to Pandas/intel.csv',
        index_col='Date', parse_dates=True)

# I create a Numpy array using the data in the column 'Close'
"""close_values = df['Close'].values
plt.plot(close_values)
plt.show()
"""

# I create a plot using 'Close' and giving it attributes
df['Close'].plot(color='g',style='-',legend=True,title='Stock price',
    xlabel='Dates',ylabel='Sterling pounds')
# g for green, - for line style
plt.axis(('2017','2018',0,60))
#plt.title('Stock price')
#plt.show()
plt.savefig('df_close.png')
