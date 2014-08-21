from networkx import *
import numpy as np
import matplotlib.pyplot as plt
no_nodes=1000
pp = []
gg = []

#Generator for 0 to 1.

#print float_range(0,1,0.01)


a=np.linspace(0,1,100)
for p in a:
    g= watts_strogatz_graph(no_nodes, 4, p)
    pp.append(density(g))
    gg.append(average_clustering(g))
#print density(g), average_clustering(g)
#print pp,gg
plt.plot(a,gg)
plt.show()
plt.plot(a,pp)
plt.show()
