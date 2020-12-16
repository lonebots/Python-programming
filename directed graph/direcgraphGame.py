import networkx as nx
import random
import matplotlib.pyplot as plt
import operator
from operator import itemgetter


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

#distribute points function
def distribute_points(G,points):
    nodes=list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
    for n in nodes:
        out=list(G.out_edges(n))
        if(len(out)==0):
            new_points[n]=new_points[n]+points[n]
        else:
            share=points[n]/len(out)
            for(src,tgt) in out:
                new_points[tgt]=new_points[tgt]+share
    return new_points


#keep distributing
def keep_distributing(points,G):
    while(1):
        new_points=distribute_points(G,points)
        print(new_points)
        points=new_points
        stop=input('press # to stop or anyother key to continue')
        if stop=='#':
            break
    return new_points


def rank_by_points(points):
    #we will be using the dictionary
    d={}
    for i in range(len(points)):
        d[i]=points[i]
    #sorting the dictionary
    print(*sorted(d.items(),key=lambda f:f[1]),sep="\n",end="\n\n")


#create a directed graph
G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])

G=add_edges(G);#adding the edges

#visualize the graph
nx.draw(G,with_labels=True)
#plt.show()

#point initialisation
points=assign_points(G)

#keep distributing
final_points=keep_distributing(points,G)

#rank the nodes by points
rank_by_points(final_points)

#default networkx function
result=nx.pagerank(G)
print(*sorted(result.items(),key=lambda f:f[1]),sep="\n",end="\n\n")