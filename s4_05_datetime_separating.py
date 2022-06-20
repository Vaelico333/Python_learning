import pandas as pd
sales_data = pd.read_csv('../../sample_data/04 Time Series/sales_data.csv',parse_dates=True, index_col='InvoiceDate')

morning_sales = sales_data['Quantity']['2010-12-01']

#I create a variable containing the maximum sales based on the hourly rate
high_quantity = morning_sales.resample('H').max()
print(high_quantity)

#Same for minimum sales:
low_quantity = morning_sales.resample('H').min()
print(low_quantity)
