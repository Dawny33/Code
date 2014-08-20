import heapq


''' Input arguments for the dijkstra module:
adj:   Adjacency lists (taken as a python dictionary)
costs: The costs of each edge (taken as a Python dictionary)
s:     The starting vertex (source)
t:     The ending vertex   (destination)
'''


'''Algorithm: The entire info. i.e. the cost, parent node and the target node 
is stored in a heap, and then popped accordingly.

If the popped node is not in the visited set, we then append the popped edge into the set.
'''


def dijkstra(adj, costs, s, t):


#Q is the priority queue.
    Q = [] 
# vertex : minimal distance
    d = {s: 0} 
# vertex : [d[v], parent_v, v]  {distances from parent node.}
    Qd = {}    
# predecessor
    p = {}     

    visited_set = set([s])

    for v in adj.get(s, []):
        d[v] = costs[s, v]
        item = [d[v], s, v]
        heapq.heappush(Q, item)
        Qd[v] = item


    while Q:
        #print Q
        cost, parent, u = heapq.heappop(Q)
        if u not in visited_set:
            print 'selected node:', u
            p[u]= parent
            visited_set.add(u)
            if u == t:
                return p, d[u]
            for v in adj.get(u, []):
                if d.get(v):
                    if d[v] > costs[u, v] + d[u]:
                        d[v] =  costs[u, v] + d[u]
                        Qd[v][0] = d[v]    
                        Qd[v][1] = u       
                        heapq._siftdown(Q, 0, Q.index(Qd[v]))
                else:
                    d[v] = costs[u, v] + d[u]
                    item = [d[v], u, v]
                    heapq.heappush(Q, item)
                    Qd[v] = item

    return None

#Make edges as given in the cost dictionary.
def make_undirected(cost):
    ucost = {}
    for k, w in cost.iteritems():
        ucost[k] = w
        ucost[(k[1],k[0])] = w
    return ucost

#Now, we enter the input and call the Dijkstra's module.
if __name__=='__main__':

    # adjacecy list (input)
    adj = { 1: [2,3,6],
            2: [1,3,4],
            3: [1,2,4,6],
            4: [2,3,5,7],
            5: [4,6,7],
            6: [1,3,5,7],
            7: [4,5,6]}

    # edge costs (edge lengths or costs)
    cost = { (1,2):5,
            (1,3):9,
            (1,6):14,
            (2,3):10,
            (2,4):15,
            (3,4):12,
            (3,6):2,
            (4,5):6,
            (5,6):9,
            (4,7):2,
            (5,7):1,
            (6,7):12}

    cost = make_undirected(cost)

    s, t = 1, 7
    predecessors, min_cost = dijkstra(adj, cost, s, t)
    c = t
    path = [c]
    print 'min cost:', min_cost
    while predecessors.get(c):
        path.insert(0, predecessors[c])
        c = predecessors[c]

    print 'shortest path:', path

