#graph in python
#concepts of graph theory
#over the facebook friend graphs data.
#using the networkx

#this will prove the we have 6 degree of separation
#on 6 degree you will get to the entire population to your comparitve relation
#thus you will reach the destination with the shortest path.

import networkx as nx
import numpy as np

#graph G
G = nx.read_edgelist("facbook_combined.txt")
#node of the graph is a list
N = list(G.nodes())

#for each pair of edges we are finding the shortest path
spll = []
for u in N:
    for v in N:
        if (u != v):
            l = nx.shortest_path_length(G, u, v)
            print("Shorted path btw", u, "and", v"is ", l)
            spll.append(l)
#shortest path is calculated and stored in spll

#finding the minimum value from the shortest path length
min_spl = min(spll)

#finding the maximum value from the shortest path length
max_spl = max(spll)

#finding the average of the list of values
avg_spl=np.average(spll)