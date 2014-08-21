from networkx import *
no_nodes=1000
for p in [ 0.1, 0.2, 0.3]:
    g = watts_strogatz_graph(no_nodes, 4, p)
print density(g), average_clustering(g) 
