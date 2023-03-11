import pandas as pd
# Traditional way
# df = pd.read_csv('../../sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv')

# Indirect way, sometimes useful. I add an empty header because it doesn't have one
# Then I add the list as header with the attribute 'names'
# I introduce the attribute na_values to tell python when to show NaN
filepath = '../../sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv'
column_names = ['App','Rating','Reviews','Size','# of installs','Type','Price','Last Updated']
df = pd.read_csv(filepath, header=None, names=column_names, na_values='-1')

# I define a new index based on a column in the file, could be a list etc
df.index = df['Last Updated']

# Then I modify the output so I just get the data I want
new_columns = ['App','Reviews','Rating']
df = df[new_columns]

# Now I'll share the data using the arg to_csv, creating a new file
out_csv = 'Google Play Data'
df.to_csv(out_csv)

# I can create excel files too (note that I need to include the extension 'xlsx'):
out_xlsx = 'Google Play Data EXCEL.xlsx'
df.to_excel(out_xlsx)
