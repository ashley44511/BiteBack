import pickle
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
        

    # Print the graph
    def print_graph(self):
        for key, value in self.adjList.items():
            print(f"{key}: {value}")
        
            #print("Vertex " + str(i) + ": ", end="")
             
            #for j in self.adjList[i]:
               # print("->", end =" ")
               # print(str(j), end = "")
                 
            #print(" \n")


if __name__ == "__main__":
    # Create graph and edges
    graph = Graph()
    graph.add_edge("milk", "protein", 5)
    graph.add_edge("milk", "fat", 6)
    graph.add_edge("sausage", "protein", 2)
    graph.add_edge("banana", "vitamin C", 3)
    graph.add_edge("mango", "vitamin D", 2)

    graph.print_graph()

    # once graph is fully loaded 
    with open("data_graph.pickle", "wb") as file:
        pickle.dump(graph, file)
        print ("Graph successfully pickled!")
