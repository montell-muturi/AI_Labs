import networkx as nx
import matplotlib.pyplot as plt

from gbfs import GreedyBFS as greedybfs

plt.figure(figsize=(13,6))

#creeating graph object
Graph = nx.Graph()

#adding nodes to grpah
nodes = ["SportsComplex", "Siwaka", "Ph.1A", "Ph.1B", "Phase2", "J1", "Mada", "Phase3", "STC", "ParkingLot"]
Graph.add_nodes_from(nodes)
Graph.nodes()

#adding edges and weights between nodes
Graph.add_edge("SportsComplex","Siwaka",weight="450")
Graph.add_edge("Siwaka","Ph.1A",weight="10")
Graph.add_edge("Siwaka","Ph.1B",weight="230")
Graph.add_edge("Ph.1A","Ph.1B",weight="100")
Graph.add_edge("Ph.1A","Mada",weight="850")
Graph.add_edge("Ph.1B","STC",weight="50")
Graph.add_edge("Ph.1B","Phase2",weight="112")
Graph.add_edge("STC","Phase2",weight="50")
Graph.add_edge("STC","ParkingLot",weight="250")
Graph.add_edge("Phase2","Phase3",weight="500")
Graph.add_edge("Phase2","J1",weight="600")
Graph.add_edge("Phase3","ParkingLot",weight="350")
Graph.add_edge("J1","Mada",weight="200")
Graph.add_edge("Mada","ParkingLot",weight="700")

#add heuristics to nodes
heuristics_list = {
    ("SportsComplex") : 730,
    ("Siwaka") : 405,
    ("Ph.1A") : 380,
    ("Ph.1B") : 280,
    ("Phase2") : 210,
    ("J1") : 500,
    ("Mada") : 630,
    ("Phase3") : 160,
    ("STC") : 213,
    ("ParkingLot") : 0
}
nx.set_node_attributes(Graph, heuristics_list, "heuristics")

heuristics = nx.get_node_attributes(Graph, "heuristics")

#position nodes visually
Graph.nodes["SportsComplex"]['pos']=(-5,5)
Graph.nodes["Siwaka"]['pos']=(-3,5)
Graph.nodes["Ph.1A"]['pos']=(0,5)
Graph.nodes["Ph.1B"]['pos']=(0,3)
Graph.nodes["Phase2"]['pos']=(2,3)
Graph.nodes["J1"]['pos']=(5,3)
Graph.nodes["Mada"]['pos']=(7,3)
Graph.nodes["STC"]['pos']=(0,0)
Graph.nodes["Phase3"]['pos']=(5,0)
Graph.nodes["ParkingLot"]['pos']=(5,-2)

node_positions = nx.get_node_attributes(Graph,'pos')

#create greedy bfs instance
path_gbfs = greedybfs(heuristics)

#determine best path and store it in a list
walk = path_gbfs.traverse(Graph, "SportsComplex", "ParkingLot")

#color the nodes and edges
node_col = ['lightblue' if not node in walk else 'lightgreen' for node in Graph.nodes()]
print(list(zip(walk, walk[1:])))
edge_col = [ 'black' if not edge in list(zip(walk, walk[1:])) else 'lightgreen' for edge in Graph.edges()]
arc_weight=nx.get_edge_attributes(Graph,'weight')

nx.draw_networkx(Graph, node_positions,node_color= node_col, node_size=400, font_size = 8)
nx.draw_networkx_edges(Graph,node_positions,width = 2,edge_color =edge_col)
nx.draw_networkx_edge_labels(Graph,node_positions,edge_labels = arc_weight, font_size = 8)

#use pyplot to show the graph figure
plt.show()