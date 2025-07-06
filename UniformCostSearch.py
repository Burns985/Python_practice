import math

def findMin (frontier):
	# returns that node in the frontier which has a lowest cost minV-math.inf
	node=''
	for i in frontier:
		if minV>frontier [i] [1]:
		minV=frontier[i] [1]
		node = i
	return node


def actionSequence (graph, initialState, goalState):
	# returns a list of states starting from goal state moving upwards towards # parents until root node is reached
	solution= [goalState]
	currentParent=graph [goalState].parent
	while current Parent!=None:
		solution.append (currentParent)
		currentParent = graph [currentParent].parent
	solution.reverse()
	return solution

class Node:
	#state = state
	# class variable shared by all instances
	def init (self, state, parent, actions, totalCost):
		self.state = state # instance variable unique to each instance self.parent = parent
		self.actions = actions # we are not saving actions themselves,
					# only output states of those actions

		self.totalCost = totalCost


def UCS ():
	initialState = 'C'
	goalState = 'B'
	# we think of a graph as a dictionary, items comprise of nodes, wher
	# each node has a key and a value. Key is simply the state of the no
	# and value are actual attributes that node object
##
	graph = {'A': Node ('A', None, 'B': Node('B', None, 'C': Node('C', None, 'D': Node('D', None, 'E': Node('E', None, 'F': Node('F', None, 'G': Node ('G', None, [('C',3)],
	[('B', 6), [('A', 6),
	('C', 9), ('E',1)], 0), ('D',3), ('E',4)], 0),
	[('A', 9), [('B',3), [('A',1),
	('F',2), ('G',3)], 0),('E',5),('F',7)], 0),('B', 4),
	('D',5), ('F', 6)],[('C', 2),('E', 6),('D',7)], 0),0)}
	frontier = dict()
	frontier [initialState] = (None, 0)
	explored=[] # parent of initial node is None and its cost is 0
