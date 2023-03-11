import pandas as pd
sales_data = pd.read_csv('../../sample_data/04 Time Series/sales_data.csv',parse_dates=True, index_col='InvoiceDate')

# I create a variable that contains the maximum range of the 2 weekly sales
weekly_max = sales_data.resample('2W').sum().max()
print(weekly_max)

# If I just want to see the Quantity column:
weekly_max = sales_data.loc[:, 'Quantity'].resample('W').sum()
print(weekly_max)
