import networkx as nx
import random
import matplotlib.pyplot as plt


#add_edges in G
def add_edges(G):
    nodes=list(G.nodes())
    for s in nodes:
        for t in nodes:
            if s!=t:
                r=random.random()#simulating a coin toss
                if r<=0.5:
                    G.add_edge(s,t)
    return G

#assigning points
def assign_points(G):
    nodes=list(G.nodes())
    p=[]
    for each in nodes:
        p.append(100)#initializing points to 100
    return p
    

#create a directed graph
G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])

G=add_edges(G);#adding the edges

#visualize the graph
nx.draw(G,with_labels=True)
plt.show()

#point initialisation
points=assign_points(G)


