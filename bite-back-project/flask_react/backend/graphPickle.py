import pickle
from dataCleaning import loadData 
import random


# adjacency list in python inspiration: https://www.programiz.com/dsa/graph-adjacency-list

class Graph:
    def __init__(self):
        # graph is a dictionary of sets, with each value in the set being a tuple in the format: (nodeName, weight)
        self.adjList = {}
        self.size = 0 #nodes
        self.edges = 0 #one undirected edge is one edge

    # Adds edges
    def add_edge(self, nodeTo, nodeFrom, weight):
        #have to store edge twice since this graph is undirected
        #check that node not already in graph
        if (nodeFrom not in self.adjList):
            self.size += 1
            self.adjList[nodeFrom] = {(nodeTo, weight)}
        else:
            self.adjList[nodeFrom].add((nodeTo, weight))

        if (nodeTo not in self.adjList):
            self.size += 1
            self.adjList[nodeTo] = {(nodeFrom, weight)}
        else:
            self.adjList[nodeTo].add((nodeFrom, weight))
        
        self.edges += 1

    def load_data(self, df):
        #this function is used to load the dataframe into the graph
        for index, row in df.iterrows():
            food = row.iloc[0]
            for nutrient, amount in zip(df.columns[1:], row.iloc[1:]):
                self.add_edge(food, nutrient, amount)

    def getFood(self, foodName):
        # this returns the entire list of edges to a food as a dict, which should be ALL nutrients
        adjList = self.adjList[foodName]
        nutrients = {}
        for nutrient in adjList:
            nutrients[nutrient[0]] = nutrient[1]

        return nutrients
    
    def getHighestNutrientFoods(self, nutrientName, amountNeeded):
        # this returns all foods that contain the amount of a nutrient needed (within a 20% amount needed unit threshold - ensures returning something)
        # this list contains foods with the highest amount of the input nutrient
        threshold = amountNeeded * 0.2
        adjList = self.adjList[nutrientName]
        goalFoods = []
        for food in adjList:
            if (amountNeeded - threshold) <= food[1] <= (amountNeeded + threshold):
                goalFoods.append(food[0])
         
        return goalFoods

    def getNutrient(self, foodName, nutrientName):
        #returns value of a specific nutrient for food
        nutrients = self.getFood(foodName)
        for nutrient in nutrients:
            if nutrient[0] == nutrientName:
                return nutrient[1]
            
    def mealNutrition(self, meal):
        # returns base nutrition of an input meal as a dictionary
        totalNutrition = {}
        for food in meal:
            foodNutrition = self.getFood(food)
            for nutrient, amount in foodNutrition.items():
                if nutrient in totalNutrition:
                    totalNutrition[nutrient] += amount
                else:
                    totalNutrition[nutrient] = amount

        return totalNutrition

    def neededNutrients(self, meal):
        # returns nutrients needed based on daily intake
        # recommended daily intake of nutrients. taken from
        # https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels
        # initiated as dictionary of form 'nutrient name: amount"
        # total nutrients needed daily
        daily_intake = {
            "Alpha Carotene": 0,
            "Beta Carotene": 0,
            "Beta Cryptoxanthin": 0,
            "Carbohydrate": 275,
            "Cholesterol": 300,
            "Choline": 2300,
            "Fiber": 28,
            "Lutein and Zeaxanthin": 0,
            "Lycopene": 0,
            "Niacin": 16,
            "Protein": 50,
            "Retinol": 0,
            "Riboflavin": 1.3,
            "Selenium": 55,
            "Sugar Total": 50,
            "Thiamin": 1.2,
            "Water": 0,
            "Monosaturated Fat": 0,
            "Polysaturated Fat": 0,
            "Saturated Fat": 20,
            "Total Lipid": 78,
            "Calcium": 1300,
            "Copper": 0.9,
            "Iron": 18,
            "Magnesium": 420,
            "Phosphorus": 1250,
            "Potassium": 4700,
            "Sodium": 2300,
            "Zinc": 11,
            "Vitamin A - RAE": 900,
            "Vitamin B12": 2.4,
            "Vitamin B6": 1.7,
            "Vitamin C": 90,
            "Vitamin E": 15,
            "Vitamin K": 120
        }
        
        # nutrients in the dataset that didn't have daily recommendations 
        irrelevant = ["Alpha Carotene", "Beta Carotene", "Beta Cryptoxanthin", "Lutein and Zeaxanthin", 
                  "Lycopene", "Retinol", "Water", "Monosaturated Fat", "Polysaturated Fat"]
        
        # total nutrients in user meal
        mealNutrition = self.mealNutrition(meal)

        # determine nutrients needed
        goal = {}
        needed = {}
        for nutrient in daily_intake:
            # divide daily value by 3 because this is one meal of 3 meals in a day
            goal[nutrient] = daily_intake[nutrient] / 3
            needed[nutrient] = daily_intake[nutrient] / 3

        for nutrient, amount in mealNutrition.items():
            needed[nutrient] -= (amount)
        return needed, goal # returning dictionaries in format 'nutrient name: amount needed'

    def print_graph(self):
        # Print the graph - used to check proper loading during development
        for key, value in self.adjList.items():
            print(f"{key}: {value}")

    def getSuggestions(self, neededNutrients, goalNutrients):
    # function to parse graph and find 5 food suggestions to improve meal. 
    # ideally would like both suggestion functions to have each suggestion focus on a different nutrient, like the top 5 most needed
        suggestions = {}
        percentage = {}
        for nutrient in neededNutrients:
            # determining top 5 needed by highest percentage needed
            if goalNutrients[nutrient] == 0:
                pass  # don't store nutrients not needed or with goal met
            elif (neededNutrients[nutrient] / goalNutrients[nutrient]) < 0:
                pass
            else:
                percentage[nutrient] = neededNutrients[nutrient] / goalNutrients[nutrient]

        # sorts highest to lowest percentage (highest percentage means highest amount still needed)
        sortedPercentage = dict(sorted(percentage.items(), key=lambda item: item[1], reverse=True))
        top_5_needed = list(sortedPercentage.items())[:5] #dictionary with nutrient name : % amount needed

        top_5_dict = {}
        for i in top_5_needed:
            # change back to numerical from percentage needed
            foodName = i[0]
            top_5_dict[foodName] = neededNutrients[foodName]

        # find foods that meet top_5_needed
        for nutrient in top_5_dict:
            suggestions[nutrient] = (random.choice(self.getHighestNutrientFoods(nutrient, top_5_dict[nutrient])))
            
        # suggestions in format {vitamin : food suggestion}
        return suggestions  
        
def pickleGraph():
    # Create graph, Load DF, and insert nodes/edges
    graph = Graph()
    df = loadData()
    graph.load_data(df)

    # example graph for testing :
    '''
    graph.add_edge("milk", "protein", 5)
    graph.add_edge("milk", "fat", 6)
    graph.add_edge("sausage", "protein", 2)
    graph.add_edge("banana", "vitamin C", 3)
    graph.add_edge("mango", "vitamin D", 2)
    '''

    # once graph is fully loaded (only need to do this once since it stores the whole data set - point is to reduce runtime when using webapp)
    with open("data/data_graph.pickle", "wb") as file:
        pickle.dump(graph, file)
        print ("Graph successfully pickled!")


# this code was used to pickle the data from the dataframe - not needed anymore
'''
if __name__ == "__main__":
    # Create graph, Load DF, and insert nodes/edges
    graph = Graph()
    df = loadData()
    graph.load_data(df)

    # example graph for testing :
    
    graph.add_edge("milk", "protein", 5)
    graph.add_edge("milk", "fat", 6)
    graph.add_edge("sausage", "protein", 2)
    graph.add_edge("banana", "vitamin C", 3)
    graph.add_edge("mango", "vitamin D", 2)
    

    # once graph is fully loaded (only need to do this once since it stores the whole data set - point is to reduce runtime when using webapp)
    with open("data/data_graph.pickle", "wb") as file:
        pickle.dump(graph, file)
        print ("Graph successfully pickled!")
'''