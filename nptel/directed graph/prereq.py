import networkx as nx
from networkx.classes.reportviews import NodeView
import random

#creating an undirected graph
U=nx.Graph()

#creating a directed graph
G=nx.DiGraph()

#viewing the nodes in graph G
G.nodes()

#adding nodes to the graph
G.add_nodes_from([i for i in range(5)])

#this is nodeview datatype so we should convert it in to list for doing the operations in it smoothly
print(G.nodes())

#we also have to specify the incoming and outgoing edges in the graph
#print(type(list(G.nodes())))

#adding random edges
n=len(list(G.nodes()))
for i in range(n):
    s=random.randint(0,n)
    d=random.randint(0,n)
    if(s!=d):
        G.add_edge(s,d) 

print(G.out_edges)
print(G.in_edges)