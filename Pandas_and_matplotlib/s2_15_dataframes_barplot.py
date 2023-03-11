import pandas as pd
import matplotlib.pyplot as plt

# Import the data file
stock_prices = pd.read_csv('../../sample_data/03 Data Analysis/intel_stock_price.csv')

# Print to check
#print(stock_prices)

# Create a bar plot
stock_prices.plot(kind='bar',x='month',y='price',color='red',title='Stock price per month')

#Name the axis
plt.ylabel('Closing price in Pounds')
plt.xlabel('Month')

# Show the plot
plt.show()
