import pandas as pd

# Read in the data file
play_data = pd.read_csv('../../sample_data/02 Introduction to Pandas/googleplaystore.csv')

# Print the dataframe to make sure it's right
#print(play_data)

# Print all the rows with data equal or greater than five
print(play_data[play_data['Rating']>=5])

# Create a conditional filter to find all the 'Arcade' in the 'Genre' column
arcade_data = play_data[play_data['Genres']=='Arcade']

# Print the new arcade data
print(arcade_data)
