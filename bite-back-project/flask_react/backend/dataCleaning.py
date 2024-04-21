# run once at the beginning of starting the React App
# pip install pandas
# requirements.txt? we'll see later

import pandas as pd
# import graphPickle as graph
# import hashPickle as hash

def loadData():
    df = pd.read_csv("data/food.csv")
    remove = 'Category'
    remove_again = 'Nutrient Data Bank Number'
    df.drop(remove, axis=1, inplace=True)
    df.drop(remove_again, axis=1, inplace=True)
    return df

# dropped two columns not needed for work, and return dataframe to use in other files