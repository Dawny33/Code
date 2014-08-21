from networkx import *
import matplotlib.pyplot as plt

no_nodes=1000
pp = []
gg = []
o = [ 0.1, 0.2, 0.3]
for p in [ 0.1, 0.2, 0.3]:
    g = watts_strogatz_graph(no_nodes, 4, p)
    pp.append(density(g))
    gg.append(average_clustering(g))
    
    #print density(g), average_clustering(g)
print pp,gg

plt.plot(o,gg)


plt.show() 

plt.plot(o,pp)
plt.show()