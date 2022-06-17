import pandas as pd
import matplotlib.pyplot as plt

# Import the data file
life = pd.read_csv('../../sample_data/03 Data Analysis/irish_life_expec.csv')

# Print to check
#print(life)

# Create scatter plot with x=year and y=life expectancy
life.plot(kind='scatter',x='year',y='life expec')

# Add a Title
plt.title('Life expectancy in Ireland')

# Add x and y axis labels
plt.xlabel('Year')
plt.ylabel('Age')
plt.show()
