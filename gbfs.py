import networkx as nx

from collections import defaultdict

class GreedyBFS:

    def __init__(self, heuristics):
        self.open_queue = []
        self.closed_queue = []
        self.path = []
        self.children = []
        self.heuristics = heuristics

    #function to get all child nodes excluding those already searched
    def getsubnodes(self, graph, node):
        nb = nx.neighbors(graph, node)
        for node in nb:
            if node not in self.closed_queue:
                self.children.append(node)

    #function to determine most feasible child node in the open queue
    def getlowestheuristic(self, open_queue_nodes):
        lowest_heuristic = 730
        for node in open_queue_nodes:
            if self.heuristics[node[0]] < lowest_heuristic:
                best_node = node[0]
        return best_node

    def traverse(self, graph, start, destination):
        #append current node to the open queue
        self.open_queue.append(start)
        #append current node to path list
        self.path.append(start)
        #get all subnodes of current node and add them to a children-nodes list
        self.children.append(self.getsubnodes(graph, start))
        #remove node from open queue and put it in closed queue
        self.open_queue.remove(start)
        self.closed_queue.append(start)
        #add all children nodes to open queue
        self.open_queue.append(self.children)
        #get the most feasible node from the open queue
        best_node = self.getlowestheuristic(self.open_queue)
        print("Walk to: " + best_node)
        #clear all nodes from open queue and children queue
        self.open_queue.clear()
        self.children.clear()
        #check for destination
        if best_node == destination:
            self.path.append(best_node)
            print("You have reached your destination")
            return self.path
        #recursively call function onto most feasible child node
        return self.traverse(graph, best_node, destination)

    