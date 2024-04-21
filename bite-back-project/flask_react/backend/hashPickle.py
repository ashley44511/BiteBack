import pickle
from dataCleaning import loadData
df = loadData()

# Referenced Geeks for Geeks for Hash Table implementation
# https://www.geeksforgeeks.org/implementation-of-hash-table-in-python-using-separate-chaining/
# changed it up though since we don't need all of their functions and used open addressing instead

# how each food is stored in the HT
class Entry:
    def __init__(self, food, nutrients):
        self.food = food
        self.nutrients = nutrients  
    # food = name of food | nutrients = nutrition of the food
    # for hashtable of each nutrient, self.nutrients = amount of nutrient in that food

class HashTable:
    # constructor for HT
    def __init__(self):
        self.size = 0
        self.table = [None] * 7083
        # 7083 rows in the table
      
    # inserting into HT
    def insert(self, food, nutrition):
        index = hash(food) % 7082
        
        if self.table[index] is None:
            self.table[index] = Entry(food, nutrition)
            self.size += 1
        else:
            # linear probing is simpler to implement and more space efficient
            while self.table[index] is not None:
                index += 1
                if index == 7083:
                    index = 0
            self.table[index] = Entry(food, nutrition)
            self.size += 1
        
    # searching through HT to find food, given its name
    def search(self, food):
        index = hash(food) % 7082
        while self.table[index].food != food:
            index += 1
            if index == 7083:
                index = 0
        
        return self.table[index].nutrients
        # returning the only the nutrients

    def meal_nutrition(self, meal):
        # returns the base nutrition of an input meal
        total = {}
        for food in meal:
            nutrition = self.search(food)
            servings = meal[food]
            for nutrient, amount in nutrition.items():
                if nutrient in total:
                    total[nutrient] += servings * amount
                else:
                    total[nutrient] = servings * amount
        return total

    # determing how many user nutrients needs
    def needed_nutrients(self, meal):
        # recommended daily intake of nutrients. taken from
        # https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels
        # initiated as dictionary of form 'nutrient name: amount"
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
        total = self.meal_nutrition(meal)
                    
        # determining nutrients needed
        goal = {}
        needed = {}
        for nutrient, value in daily_intake:
            # divide daily value by 3 because this is one meal of 3 meals in a day
            goal[nutrient] = value / 3
            needed[nutrient] = value / 3
        
        for food, amount in total.items():
            needed[food] -= (amount)    
        return needed, goal # returning a dictionary in format 'nutrient name: amount needed'
    
    def getSuggestions(self, neededNutrients):
        # TODO
        # function to parse hash map and find 5 food suggestions to improve meal. 
        # ideally would like both suggestion functions to have each suggestion focus on a different nutrient, like the top 5 most needed
        suggestions = []

        return suggestions

if __name__ == "__main__":
    ht = HashTable()
    # iterate through each row of dataframe and store food name + nutritional content
    for index, row, in df.iterrows():
        food = row.iloc[0]
        nutrition = {}
        for nutrient, amount in zip(df.columns[1:], row.iloc[1:]):
            nutrition[nutrient] = amount
        ht.insert(food, nutrition)

     
    # after hash data is loaded and saved
    with open("data/data_hash.pickle", "wb") as file:
        pickle.dump(ht, file) 
        print("Hash map successfully pickled!")