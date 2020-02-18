class Node:
	def __init__(self,state,level,fval,parent=None):
		self.state =  state
		self.level = level
		self.fval = fval
		self.parent = parent

	def generate_children(self,parent_node):
		x,y = self.find(self.state,0)

		possible_moves = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
		children = []
		for i in possible_moves:
			child = self.shift(self.state,x,y,i[0],i[1])
			if child is not None:
				child_node = Node(child,self.level+1,0,parent_node)
				children.append(child_node)

		return children

	def copy(self,root):
		#Copy function to create a similar matrix of the given node
		temp = []
		for i in root:
			t = []
			for j in i:
				t.append(j)
			temp.append(t)
		return temp

	def shift(self,state,x1,y1,x2,y2):
		# Move the blank space in the given direction and if the position value are out
		# of limits then return None
		if x2 >= 0 and x2 < len(self.state) and y2 >= 0 and y2 < len(self.state):
			temp_puz = []
			temp_puz = self.copy(state)
			temp = temp_puz[x2][y2]
			temp_puz[x2][y2] = temp_puz[x1][y1]
			temp_puz[x1][y1] = temp
			return temp_puz
		else:
			return None


	def find(self,state,x):
		# Specifically used to find the (x,y) coordinates of the empty tile (0)
		for i in range(3):
			for j in range(3):
				if state[i][j] == x:
					return i,j

class Solution:

	def __init__(self):
		self.open = [] #initialize open list
		self.closed = [] #intialize closed list

	def print_state(self,state):
		print ("-------------")
		print ("| %i | %i | %i |" % (state[0][0], state[0][1], state[0][2])) 
		print ("-------------")
		print ("| %i | %i | %i |" % (state[1][0], state[1][1], state[1][2])) 
		print ("-------------")
		print ("| %i | %i | %i |" % (state[2][0], state[2][1], state[2][2])) 
		print ("-------------")


	def hval(self,state):
		new = state[:] #copy state

		manhattanDistanceSum = 0
		

		for x in range(3): #traversing rows
			for y in range(3): #traversing cols

				value = new[x][y]

				if (value != 0): #dont compare for empty tile
					targetX = ((value) // 3)
					targetY = ((value) % 3)


					dx = x - targetX
					dy = y - targetY

					manhattanDistanceSum += abs(dx) + abs(dy)

		return manhattanDistanceSum

	def fval(self,g,h):
		fval = g + h 
		# g =distance between sucessor and current node (basically its level)
		# h = heuristic value (manhattan distance)

		return fval

	def astar(self):
		initial_state = [[7,2,4],[5,0,6],[8,3,1]]
		goal = [[0,1,2],[3,4,5],[6,7,8]]

		start = Node(initial_state,0,0,None)
		#initialize starting node
		start.fval = self.fval(start.level,self.hval(start.state))
		#compute fval of starting node
		self.open.append(start)
		#add starting node to OPEN list to ensure that it enters the WHILE loop

		while (len(self.open) != 0):
			self.open = sorted(self.open,key = lambda x: x.fval,reverse=False)
			

			#sort OPEN list by the fval of each node
			current = self.open.pop(0)
			#since OPEN list already sorted pop the first element out of the list
			print(current.state)

			if (current.state == goal): #if the current state == goal state then solution reached				
				return self.path(current)

			#since we checked if current state == goal state; add to CLOSED list
			self.closed.append(current)


			#for each succesosr
			for i in current.generate_children(current):
				i.fval = self.fval(i.level, self.hval(i.state))

				#### check if successor d.n.e. in closed list
				skip = 0
				for j in self.closed:
					if (j.state == i.state):
						skip+=1
						break

				if (skip >0):
					continue # if exists then skip for loop once
				

				#### check if successor d.n.e. in open list
				count = 0
				for k in self.open:
					if (k.state==i.state):
						count +=1
						break
						

				if (count == 0):
					self.open.append(i) # if d.n.e. then add to OPEN list
				else:

					actual_node = k

					if (i.level < actual_node.level): #checking if better g score(level) for same node
						actual_node.level = i.level
						actual_node.fval = i.fval
						actual_node.parent = i.parent #change parent to better (earlier) parent


				# this is to prevent re-iterating on already expanded nodes

	def bfs(self):
		initial_state = [[7,2,4],[5,0,6],[8,3,1]]
		goal = [[0,1,2],[3,4,5],[6,7,8]]

		start = Node(initial_state, 0, 0, None)	

		self.open.append(start)

		while (len(self.open) != 0):

			current = self.open.pop(0)
			self.closed.append(current)	#mark state as visited

			#check is state is the goal state
			if (current.state == goal):
    				return self.path(current)
			
			#for each successor
			for i in current.generate_children(current):
					print(i.state)

					#### check if successor has been visited yet
					count = 0
					for j in self.closed:
						if (j.state==i.state):
							count +=1
							break
					
					#if not visited, queue to OPEN list
					if count==0:
								self.open.append(i)	

	def path(self,node): #constructs the path from node to start use node.parent (from root to top)

		path_list = []
		while (node.parent != None):
			path_list.append(node.state.copy())
			node = node.parent

		path_list.append(node.state)

		path_list = path_list[::-1]

		for i in path_list:
			self.print_state(i)

puzzle = Solution()
# puzzle.astar()
puzzle.bfs()



