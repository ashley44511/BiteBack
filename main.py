# run when user submits their five food items
import pickle
from graphPickle import Graph
from hashPickle import Hash
# script with algorithms
graph = Graph()
hash = Hash()

# get data into classes from pickle file
with open("./data/data_graph.pickle", "rb") as graphFile:
    graph = pickle.load(graphFile)
with open("./data/data_hash.pickle", "rb") as hashFile:
    hash = pickle.load(hashFile)

graphFile.close()
hashFile.close()

if __name__ == "__main__":
    graph.print_graph()