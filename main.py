# run when user submits their five food items
import pickle
import graphPickle 
# script with algorithms

with open("./data/data_graph.pickle", "rb") as graphFile:
    graph = pickle.load(graphFile)
#graph = pickle.load(open("data/data_graph.pickle", "rb"))
#hash = pickle.load(open("data/data_hash.pickle", "rb"))

if __name__ == "__main__":
    graph.print_graph()