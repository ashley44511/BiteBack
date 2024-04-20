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

def runHash(input):
    # HASH - start time here
    
    # find current meal nutrients 
    hashMealNutrition = hash.mealNutrition(input)

    # find nutrients needed to improve meal
    # recommended daily intake of nutrients. taken from
    # https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels
    # initiated as dictionary of form 'nutrient name: amount"
    print(hash.neededNutrients(meal))

    # run algorithm for both graph and hash 


    # return 5 suggested foods - END HASH TIME


def runGraph(input):
# GRAPH - start here and record time
    # find current meal nutrients
    pass



def createPieChart(nutrients):
    # this function will take in the meal nutrients as a SET and create a pie chart of meal balance of main macros (Protein, Carbs, Fats)
    # format: 

    pass

if __name__ == "__main__":
    # get input from website
    # todo 
    # example for now
    input = "Cuban sandwich, with spread"
    meal = [input]

    time, suggestions = runHash(input)
    time, suggestions = runGraph(input)