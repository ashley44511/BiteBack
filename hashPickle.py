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
    # can maybe make a compare function here that can calculate the nutritional differences

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
        # returning the entry itself. can alter to return only the nutrients


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