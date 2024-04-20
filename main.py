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
    # recommended daily intake of nutrients. taken from
    # https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels
    # initiated as dictionary of form 'nutrient name: amount'
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
    
        
        # nutrients in the dataset that don't have daily recommendations
    
    # nutrients in the dataset that didn't have daily recommendations
    irrelevant = ["Alpha Carotene", "Beta Carotene", "Beta Cryptoxanthin", "Lutein and Zeaxanthin", 
                  "Lycopene", "Retinol", "Water", "Monosaturated Fat", "Polysaturated Fat"]


    meal = ["Cuban sandwich, with spread"]
    print(hash.neededNutrients(meal, daily_intake))

    # run algorithm for both graph and hash 


    # return 5 suggested foods