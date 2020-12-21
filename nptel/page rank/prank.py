import networkx as nx
import random
import matplotlib.pyplot as plt
import operator
from operator import itemgetter

#drawing a random directed graph
G = nx.gnp_random_graph(10, 0.5, directed=True)
nx.draw(G, with_labels=True)
#plt.show()

#taking random source node
x = random.choice([i for i in range(G.number_of_nodes())])

#initialize an empty dictionary for storing the page visits
dict_counter = {}
for i in range(G.number_of_nodes()):
    dict_counter[i] = 0

#increment the counter of source node by 1
dict_counter[x] = dict_counter[x] + 1

for i in range(100000):
    list_n = list(G.neighbors(x))
    if (len(list_n) == 0):  #if x is sink
        x = random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x] = dict_counter[x] + 1
    else:
        x = random.choice(list_n) #choose a random node from the neighbors of x
        dict_counter[x] = dict_counter[x] + 1

#print(dict_counter)

#page rank method
p=nx.pagerank(G)
#print(p)
#print(dict_counter)

sorted_p=sorted(p.items(),key=operator.itemgetter(1))#sorting the dictonary based on the values
sorted_rw=sorted(dict_counter.items(),key=operator.itemgetter(1))
print(*sorted_p,sep="\n")
print(*sorted_rw,sep="\n")