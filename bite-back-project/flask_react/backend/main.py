# run when user submits their five food items
import pickle
import os
from graphPickle import Graph, pickleGraph
from hashPickle import HashTable, pickleHash
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

    def pickleNewHash(self):
        pickleHash()

    def unpickleHash(self):
        with open(os.path.abspath("data/data_hash.pickle"), "rb") as hashFile:
            self.hash = pickle.load(hashFile)
        hashFile.close()

    def runHash(self, meal):
        # HASH - start time here
        startTime = time.time()
        
        # find current meal nutrients - this is used for visualizations
        mealNutrition = self.hash.mealNutrition(meal)

        # find nutrients needed to improve meal
        neededNutrients, goalNutrients = self.hash.neededNutrients(meal)

        # run suggestion algorithm 
        foodSuggestions = self.hash.getSuggestions(neededNutrients, goalNutrients)

        # return 5 suggested foods - END HASH TIME
        endTime = time.time()
        runTime = endTime - startTime #calculate runTime of hash 
        return runTime, foodSuggestions, goalNutrients

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
        return runTime, foodSuggestions, mealNutrition
    
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
        fig.update_layout(title_x=0.5)
        fig.update_layout(width=800, height=600)
        fig.update_layout(title_font=dict(size=24), legend_font=dict(size=16))
        fig.write_image("../src/images/macro_pie_chart.png")
        return
    
    def createBarChart(self, nutrients, goalNutrients):
        # this function will take in the nutrients of the input meal and the goal nutrients (assuming 1/3 of DV should be met by meal) and will show gap of nutreients in terms of percent
        categories = []
        percentage = []
        for nutrient in nutrients:
            if goalNutrients[nutrient] == 0:
                # skip nutrients with no DV
               continue
            else:
                percentage.append((nutrients[nutrient]/goalNutrients[nutrient]) * 100)
                categories.append(nutrient)

        # Create overlapped bar chart
        fig = px.bar(x=categories, y=percentage, barmode='overlay', labels={'x':'Nutrient', 'y':'Percent Met'},
                    title='Percentage of 1/3 Daily Value Met from Input Meal - Excludes Nutrients with no DV', color_discrete_sequence=['green'])

        goal_value = 100
        fig.add_hline(y=goal_value, line_dash='dash', line_color='red', annotation_text=f'Goal: {goal_value}',
                      annotation_position='bottom right')

        fig.update_layout(showlegend=False)
        fig.update_layout(title_x=0.5)
        fig.update_layout(width=800, height=600)

        # Save the chart as an image
        fig.write_image('../src/images/overlapped_bar_chart.png')  # Change file format as needed (e.g., 'overlapped_bar_chart.jpg')
    
    def mainImportVersion(self, input):
        # get input from website as args
        # TODO

        # load data
        self.unpickleGraph() 
        self.unpickleHash()
        # input = {"Cuban sandwich, with spread" : 1, "Milk, whole" : 2}   # example input for now format food : num servings

        # each functions compares the time it took and the foods suggested by each data structure
        hashTime, hashSuggestions, goalNutrients = self.runHash(input)
        graphTime, graphSuggestions, mealNutrition = self.runGraph(input)
        print("Hash RunTime: " + str(hashTime))
        print("Hash Suggestions: ", end = "")
        print(hashSuggestions)
        print("Graph RunTime: " + str(graphTime))
        print("Graph Suggestions: ", end = "")
        print(graphSuggestions)

        #create visualizations
        self.createPieChart(mealNutrition)
        self.createBarChart(mealNutrition, goalNutrients)


        #return hash runtime, graph runtime, graph suggestions, hash suggestions
        return graphTime, graphSuggestions, hashTime, hashSuggestions

        

        # send charts, time, and food suggestions to back end 

@api.route('/profile/', methods=['POST'])
def my_profile():
    food1Name = request.json['food1Name']
    food1Serving = request.json['food1Serving']
    food2Name = request.json['food2Name']
    food2Serving = request.json['food2Serving']
    food3Name = request.json['food3Name']
    food3Serving = request.json['food3Serving']
    food4Name = request.json['food4Name']
    food4Serving = request.json['food4Serving']
    food5Name = request.json['food5Name']
    food5Serving = request.json['food5Serving']
    input = {food1Name: food1Serving, food2Name: food2Serving, food3Name: food3Serving, food4Name: food4Serving, food5Name: food5Serving}

    main = Main()
    #hashTime, hashSuggestions
    graphTime, graphSuggestions, hashTime, hashSuggestions = main.mainImportVersion(input)
    vitaminsG = []
    vitaminsH = []
    foodsG = []
    foodsH = []

    for item in graphSuggestions:
        vitaminsG.append(item)
        foodsG.append(graphSuggestions[item])

    for item in hashSuggestions:
        vitaminsH.append(item)
        foodsH.append(hashSuggestions[item])


    response_body = {
        "suggestion1G": foodsG[0],
        "suggestion2G": foodsG[1],
        "suggestion3G": foodsG[2],
        "suggestion4G": foodsG[3],
        "suggestion5G": foodsG[4],
        "graphTime": graphTime,
        "suggestion1H": foodsH[0],
        "suggestion2H": foodsH[1],
        "suggestion3H": foodsH[2],
        "suggestion4H": foodsH[3],
        "suggestion5H": foodsH[4],
        "hashTime": hashTime,
    }

    return response_body


if __name__ == "__main__":
    main = Main()
    main.pickleNewGraph()
    main.pickleNewHash()
 
