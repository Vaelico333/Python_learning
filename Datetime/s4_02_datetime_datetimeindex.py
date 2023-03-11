import pandas as pd

datetime_string = ['12-01-2010 08:26', '12-02-2010 16:38', '12-03-2010 12:24',
 '12-05-2010 10:03', '12-05-2010 10:03']

# Prepare a format string: time_format
time_format= '%d-%m-%Y %H:%M'

# Convert the list into a datetime object
datetime_object = pd.to_datetime(datetime_string, format=time_format)
print(datetime_object)
