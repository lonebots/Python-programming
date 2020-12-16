import networkx as nx
import matplotlib.pyplot as plt

#read the file and of edges and make the directed graph
G=nx.read_edgelist(r"edgelist.txt",create_using=nx.DiGraph(),nodetype=int)

#draw the graph
nx.draw(G,with_labels=True)
plt.show()