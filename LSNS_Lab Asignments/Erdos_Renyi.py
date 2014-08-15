import random

class Node:
	def __init__(self, index):
		self.index = index
		self.neighbors = []
	def __repr__(self):
		return repr(self.index)

def randomGraph(n,p):
	vertices = [Node(i) for i in range(n)]
	edges = [(i,j) for i in xrange(n) for j in xrange(i) if random.random() < p]
	for (i,j) in edges:
		vertices[i].neighbors.append(vertices[j])
		vertices[j].neighbors.append(vertices[i])
	return edges

print randomGraph(10,0.1)
