from networkx import *
import matplotlib.pyplot as plt
no_nodes=1000
pp = []
gg = []

#Generator for 0 to 1.
def float_range(start, end, increment):
    int_start = int(start / increment)
    int_end = int(end / increment)
    for i in range(int_start, int_end):
        print i * increment

#print float_range(0,1,0.01)



for p in float_range(0,1,0.01):
    g = watts_strogatz_graph(no_nodes, 4, p)
    pp.append(density(g))
    gg.append(average_clustering(g))
#print density(g), average_clustering(g)
print pp,gg
plt.plot(o,gg)
plt.show()
plt.plot(o,pp)
plt.show()
