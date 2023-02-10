import pandas as pd

# Dictionary with the data we need
course_sales = {'course':['Python','Ruby','Excel','C++'],
    'day':['Mon','Tue','Wed','Thurs'],
    'price':[5,10,15,20],
    'sale':[2,3,5,7]
    }

# I create a data frame directly from the dictionary
df_sales = pd.DataFrame(course_sales)
print(df_sales)

# A set of lists with the data
course = ['Python','Ruby','Excel','C++']
day = ['Mon', 'Tue', 'Tue', 'Wed']
price = [5,10,15,20]
sale = [2,3,5,7]
column_labels = ['Course','Day','Price','Sale']
# A list of lists
column_names = [course,day,price,sale]

# Combine list of column labels and column names above to create a new single list
master_list = list(zip(column_labels,column_names))
print(master_list)

# Convert master list to a dictionary
sales_data = dict(master_list)

# Convert master list dictionary to a DataFrame
df_sales_1 = pd.DataFrame(sales_data)
print(df_sales_1)

# Change the labels of the columns
column_labels = ['Course','Day','Price','24h Sale']
df_sales_1.columns = column_labels
print(df_sales_1)
