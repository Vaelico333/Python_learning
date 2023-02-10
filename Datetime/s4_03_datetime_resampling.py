import pandas as pd
sales_data = pd.read_csv('../../sample_data/04 Time Series/resampling_sales_data.csv', parse_dates=True, index_col='InvoiceDate')

#print(sales_data.info())

# I create a variable containing the mean value of the weekly sales
mean_weekly = sales_data.resample('W').mean()
print(mean_weekly)

# I create a variable containing the mean value of the monthly sales
mean_monthly = sales_data.resample('M').mean()
print(mean_monthly)

# I can check for specific locations, and focus on specific columns
print(mean_weekly.loc['2010-03-21', 'Quantity'])

# Let's check the total instead of the average
sum_weekly = sales_data.resample('W').sum()
print(sum_weekly)
