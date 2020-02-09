#/usr/bin/python3
import math 
from random import randint

class Node:
    def __init__(self):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

goal = [0,1,2,3,4,5,6,7,8]

def initial():
    #user inputs state?
    state = [4,3,2,8,0,6,7,1,5]

    print ("-------------")
    print ("| %i | %i | %i |" % (state[0], state[3], state[6])) 
    print ("-------------")
    print ("| %i | %i | %i |" % (state[1], state[4], state[7]))
    print ("-------------")
    print ("| %i | %i | %i |" % (state[2], state[5], state[8])) 
    print ("-------------")   

def move_right(state):
    new = state[:] #copy state
    index = new.index(0)

    if index not in [6,7,8]:
        temp = new[index+3]
        new[index] = temp
        new[index+3] = new[index]
        return new
    else:
        return None
    
def move_left(state):
    new = state[:] #copy state
    index = new.index(0)

    if index not in [0,1,2]:
        temp = new[index-3]
        new[index] = temp
        new[index-3] = new[index]
        return new
    else:
        return None

def move_up(state):
    new = state[:] #copy state
    index = new.index(0)

    if index not in [0,3,6]:
        temp = new[index-1]
        new[index] = temp
        new[index-1] = new[index]
        return new
    else:
        return None

def move_down(state):
    new = state[:] #copy state
    index = new.index(0)

    if index not in [2,5,8]:
        temp = new[index+1]
        new[index] = temp
        new[index+1] = new[index]
        return new
    else:
        return None

def createNode(state, parent, action, cost, depth):
    return Node(state, parent, action, cost, depth)

def expandNode(node, nodes):
    #return list of expanded nodes
    newNodes = []
    
	newNodes.append( create_node( move_up( node.state ), node, "u", node.depth + 1, 0 ) )
	newNodes.append( create_node( move_down( node.state ), node, "d", node.depth + 1, 0 ) )
	newNodes.append( create_node( move_left( node.state ), node, "l", node.depth + 1, 0 ) )
	newNodes.append( create_node( move_right( node.state), node, "r", node.depth + 1, 0 ) )

    #remove if node.state reutrns None
    for i in newNodes:
        if i.state != None:
            newNodes.append(i)
    return newNodes

# def bfs(initial,goal):
#     # perform breadth-first search




        

