import pandas as pd

sales_data = pd.read_csv('../../sample_data/04 Time Series/sales_data.csv', parse_dates=True, index_col='InvoiceDate')

# Print sales_data to make sure it's working
#print(sales_data)

# Print .info()
print(sales_data.info())

# Use .loc accesor
morning_sale = sales_data.loc['2010-12-01 08:35:00':'2010-12-01 08:51:00', 'Description']
print(morning_sale)
