#managing netwrok with python
#using netwrokx library

import networkx as nx
import matplotlib.pyplot as plt
#creating a graph
G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)
#printing nodes
print(G.nodes)
print(G.edges())
#drawing graph
nx.draw(G)
plt.show()

#adding node from list or any other container
l = [4, 5, 6, 7]
H = nx.Graph()
H.add_nodes_from(l)
nx.draw(H)
plt.show()

#complete graph
I = nx.complete_graph(10)
nx.draw(I)
plt.show()

#you can also use other function like gnp_random_graph(20,0.5)
K = nx.gnp_random_graph(50, 0.4)
nx.draw(K)
plt.show()

#scale free graphs
M = nx.barabasi_albert_graph(50, 2)
nx.draw(M)
plt.show()

nx.write_gexf(G, "graph.gexf")
#you can get open this file in gefi a software. this gexf format can
#be easily opened in the tool
