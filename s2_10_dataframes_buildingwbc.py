import pandas as pd

cities = ['Leon', 'Palencia', 'Burgos', 'Soria', 'Valladolid', 'Zamora',
        'Salamanca', 'Avila', 'Segovia']

# I create a string with the name Castilla y Leon
comunidad = 'Castilla y Leon'

# Then I create a dictionary with both of the above
cyl = {'Comunidad':comunidad, 'Ciudad':cities}

# And make a dataframe from the dictionary
dfcyl = pd.DataFrame(cyl)
print(dfcyl)
