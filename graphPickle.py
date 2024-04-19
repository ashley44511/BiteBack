import pickle
import pandas as pd 
from dataCleaning import loadData


# adjacency list in python inspiration: https://www.programiz.com/dsa/graph-adjacency-list

class Graph:
    def __init__(self):
        # graph is a dictionary of sets, with each value in the set being a tuple in the format: (nodeName, weight)
        self.adjList = {}
        self.size = 0 #nodes
        self.edges = 0 #one undirected edge is one edge


    # Add edges
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
        # this returns the entire list of nodes to a food, which should be ALL nutrients
        return self.adjList[foodName]
    
    def getNutrient(self, foodName, nutrientName):
        nutrients = self.getFood(foodName)
        nutrientStr = "Data."
    
    def print_graph(self):
        # Print the graph - to check proper loading
        for key, value in self.adjList.items():
            print(f"{key}: {value}")
        


if __name__ == "__main__":
    # Create graph, Load DF, and insert nodes/edges
    graph = Graph()
    df = loadData()
    graph.load_data(df)

    # example graph :
    '''
    graph.add_edge("milk", "protein", 5)
    graph.add_edge("milk", "fat", 6)
    graph.add_edge("sausage", "protein", 2)
    graph.add_edge("banana", "vitamin C", 3)
    graph.add_edge("mango", "vitamin D", 2)
    '''

    # once graph is fully loaded (only need to do this once since it stores the whole data set)
    # with open("data/data_graph.pickle", "wb") as file:
        # pickle.dump(graph, file)
        # print ("Graph successfully pickled!")

    