import pandas as pd
import matplotlib.pyplot as plt
stock_prices = pd.read_csv('../../sample_data/03 Data Analysis/intel_amd_stock_prices.csv')

# print to check
# print(stock_prices)

# create y-columns
y_columns = ['intel', 'amd']

# name/assign Y axis
stock_prices.plot(x=('month'),y=(y_columns))

#create a title
plt.title('Stock closing price per month')

# Title for Y axis
plt.ylabel('Price (USD $)')

# Finally, show the plot
plt.show()
