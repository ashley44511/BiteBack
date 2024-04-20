# run when user submits their five food items
import pickle
from graphPickle import Graph
from hashPickle import HashTable
from hashPickle import Entry
import plotly

# script with algorithms
graph = Graph()
hash = HashTable()

# get data into classes from pickle file
with open("./data/data_graph.pickle", "rb") as graphFile:
    graph = pickle.load(graphFile)
with open("./data/data_hash.pickle", "rb") as hashFile:
    hash = pickle.load(hashFile)

graphFile.close()
hashFile.close()

def createPieChart(nutrients):
    # this function will take in the meal nutrients as a SET and create a pie chart of meal balance of main macros (Protein, Carbs, Fats)
    # format: 

    pass

if __name__ == "__main__":
    # get input from website
    # todo 

    # find current meal nutrients 


    # develop data visualizations
    createPieChart()


    # find nutrients needed to improve meal


    # run algorithm for both graph and hash 



    # return 5 suggested foods 

    