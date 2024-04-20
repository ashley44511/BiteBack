from hashPickle import HashTable
# HELP: how do i get the hash table we're using here?



# recommended daily intake of nutrients. taken from
# https://www.fda.gov/food/nutrition-facts-label/daily-value-nutrition-and-supplement-facts-labels
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
irrelevant = ["Alpha Carotene", "Beta Carotene", "Beta Cryptoxanthin", "Lutein and Zeaxanthin", 
              "Lycopene", "Retinol", "Water", "Monosaturated Fat", "Polysaturated Fat"]

meal = ["Cuban sandwich, with spread"]

# determining total nutrients consumed
total = {}
for food in meal:
    nutrition = ht.search(food)
    for nutrient, amount in nutrition.items():
        if nutrient in total:
            total[nutrient] += amount
        else:
            total[nutrient] = amount
            

# determining nutrients needed
needed = daily_intake

for food, amount in total.items():
    needed[food] -= (amount)    
print(needed)