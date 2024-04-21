# run when user submits their five food items
import pickle
from graphPickle import Graph
from hashPickle import HashTable
from hashPickle import Entry
import plotly.express as px
import time

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

def runHash(meal):
    # HASH - start time here
    startTime = time.time()
    
    # find current meal nutrients - this is used for visualizations
    mealNutrition = hash.mealNutrition(meal)

    # find nutrients needed to improve meal
    neededNutrients = hash.neededNutrients(meal)

    # run suggestion algorithm 
    foodSuggestions = hash.getSuggestions(neededNutrients)

    # return 5 suggested foods - END HASH TIME
    endTime = time.time()
    runTime = endTime - startTime #calculate runTime of hash 
    return runTime, foodSuggestions

def runGraph(meal):
# GRAPH - start time here
    startTime = time.time()
    foodSuggestions = {}
    # find current meal nutrients - this is used for visualizations
    mealNutrition = graph.mealNutrition(meal)

    # find nutrients needed to improve meal
    neededNutrients = graph.neededNutrients(meal)

    # run algorithm for both graph and hash 
    foodSuggestions = graph.getSuggestions(neededNutrients)

    # return 5 suggested foods - END HASH TIME
    endTime = time.time()
    runTime = endTime - startTime 
    return runTime, foodSuggestions
    
def createPieChart(nutrients):
    # this function will take in meal nutrients as a dict and create a pie chart of meal balance of main macros (Protein, Carbs, Fats)
    # reference: https://plotly.com/python/pie-charts/

    # only keep macronutrients (protein, carbs, fats)
    data = []
    data["Protein"] = nutrients["Protein"]
    data["Carbohydrates"] = nutrients["Carbohydrates"]
    data["Fat"] = nutrients["Total Lipid"]

    labels = list(data.keys())
    values = list(data.values())
    fig = px.pie(values=values, names=labels, title='Input Meal Macronutrient Distribution')
    fig.show() 

if __name__ == "__main__":
    # get input from website
    # TODO

    input = "Cuban sandwich, with spread"   # example input for now
    meal = [input]

    # each functions compares the time it took and the foods suggested by each data structure
    hashTime, hashSuggestions = runHash(input) 
    grapTtime, graphSuggestions = runGraph(input)

    #create visualizations
    createPieChart(hash.mealNutrition(meal))