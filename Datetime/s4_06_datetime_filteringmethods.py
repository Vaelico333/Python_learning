import pandas as pd
sales_data = pd.read_csv('../../sample_data/04 Time Series/sales_data.csv',parse_dates=True, index_col='InvoiceDate')

#Let's create a variable containing the search terms we need
search = sales_data['Description'].str.contains('POPPY')
print(search)

#Now let's see how many poppies we sold per hour
total_poppy_sales = search.resample('H').sum()
print(total_poppy_sales)
