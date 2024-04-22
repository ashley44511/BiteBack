# run when user submits their five food items
import pickle
import os
from graphPickle import Graph, pickleGraph
from hashPickle import HashTable
from hashPickle import Entry
import plotly.express as px
import plotly.io as pio
import time

from flask import Flask, request, jsonify
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

class Main:
    def __init__(self):
        # script with algorithms
        self.graph = Graph()
        self.hash = HashTable()

        # get data into classes from pickle file
        #with open("./data/data_graph.pickle", "rb") as graphFile:
            #self.graph = pickle.load(graphFile)
        #with open("./data/data_hash.pickle", "rb") as hashFile:
            #self.hash = pickle.load(hashFile)

        #graphFile.close()
        #hashFile.close()
    
    def pickleNewGraph(self):
        pickleGraph()

    def unpickleGraph(self):
        with open(os.path.abspath("data/data_graph.pickle"), "rb") as graphFile:
            self.graph = pickle.load(graphFile)
        graphFile.close()

    def runHash(self, meal):
        # HASH - start time here
        startTime = time.time()
        
        # find current meal nutrients - this is used for visualizations
        mealNutrition = self.hash.meal_nutrition(meal)

        # find nutrients needed to improve meal
        neededNutrients, goalNutrients = self.hash.needed_nutrients(meal)

        # run suggestion algorithm 
        foodSuggestions = self.hash.getSuggestions(neededNutrients, goalNutrients)

        # return 5 suggested foods - END HASH TIME
        endTime = time.time()
        runTime = endTime - startTime #calculate runTime of hash 
        return runTime, foodSuggestions

    def runGraph(self, meal):
        # GRAPH - start time here
        startTime = time.time()
        foodSuggestions = {}
        # find current meal nutrients - this is used for visualizations
        mealNutrition = self.graph.mealNutrition(meal)

        # find nutrients needed to improve meal
        neededNutrients, goalNutrients = self.graph.neededNutrients(meal)

        # run algorithm for both graph and hash 
        foodSuggestions = self.graph.getSuggestions(neededNutrients, goalNutrients)

        # return 5 suggested foods - END HASH TIME
        endTime = time.time()
        runTime = endTime - startTime 
        return runTime, foodSuggestions
    
    def createPieChart(self, nutrients):
        # this function will take in meal nutrients as a dict and create a pie chart of meal balance of main macros (Protein, Carbs, Fats)
        # reference: https://plotly.com/python/pie-charts/

        # only keep macronutrients (protein, carbs, fats)
        data = {}
        data["Protein"] = nutrients["Protein"]
        data["Carbohydrates"] = nutrients["Carbohydrate"]
        data["Fat"] = nutrients["Total Lipid"]

        labels = list(data.keys())
        values = list(data.values())
        fig = px.pie(values=values, names=labels, title='Input Meal Macronutrient Distribution', color_discrete_sequence=px.colors.diverging.Fall)
        pio.write_image(fig, "../public/macro_pie_chart.jpg")
        #fig.write_image("bite-back-project/flask_react/public/macro_pie_chart.jpg", engine="plotly")
        return
    
    def mainImportVersion(self):
        # get input from website as args
        # TODO
        self.unpickleGraph() # load data
        input = {"Cuban sandwich, with spread" : 1, "Milk, whole" : 2}   # example input for now format food : num servings

        # each functions compares the time it took and the foods suggested by each data structure
        # hashTime, hashSuggestions = self.runHash(input)
        graphTime, graphSuggestions = self.runGraph(input)
        #print("Hash RunTime: " + str(hashTime))
        #print("Hash Suggestions: ", end = "")
        #print(hashSuggestions)
        print("Graph RunTime: " + str(graphTime))
        print("Graph Suggestions: ", end = "")
        print(graphSuggestions)

        #return hash runtime, graph runtime, graph suggestions, hash suggestions
        return graphTime

        #create visualizations
        #createPieChart(hash.mealNutrition(meal))

        # send charts, time, and food suggestions to back end 


@api.route('/profile/', methods=['POST'])
def my_profile():
    main = Main()
    graphTime = main.mainImportVersion()
    response_body = {
        "name": "Nagato",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
        "result": request.json['food1Name'],
        "graphTime": graphTime
    }

    return response_body

if __name__ == "__main__":
    main = Main()
    main.pickleNewGraph()
 
