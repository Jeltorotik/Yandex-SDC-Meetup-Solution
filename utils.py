from collections import deque

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		self.parent = None
		self.direction = None
		
		self.H = 0
		self.G = 0
		

DXDYDR = [[0, -1, "L"],
		  [0,  1, "R"],
		  [1,  0, "D"],
		  [-1, 0, "U"]]
		
def get_children(x, y):
	children = []
	for dx, dy, dr in DXDYDR:
		if (x+dx, y+dy) in cells:
			child = cells[(x+dx,y+dy)]
			
			children.append([child, dr])  
	return children


def manhattan(point1, point2):
	return abs(point1.x - point2.x) + abs(point1.y - point2.y)

def pythagorean(point1, point2):
	return (point1.x - point2.x)**2 + (point1.y - point2.y)**2


def aStar(start, end, cells):
	"""
	aStar takes two tupels start, end
	then finds the shortest path between them
	and returns sequence of direction

	:param start: (x1, y1)
	:param end: (x2, y2)
	:return: e.g.: "DDRUULLDDLLRRR"
	""" 

	#The open and closed sets
	openset = set()
	closedset = set()

	#Current point is the starting point
	current = start
	
	#Add the starting point to the open set
	openset.add(current)

	#While the open set is not empty
	while openset:
		#Find the item in the open set with the lowest G + H score
		
		current = min(openset, key=lambda o:o.G + o.H)

		#If it is the item we want, retrace the path and return it
		if current == end:
			path = ""
			while current.parent:
				path += current.direction
				current = current.parent

			return path[::-1]

		#Remove the item from the open set
		openset.remove(current)

		#Add it to the closed set
		closedset.add(current)

		#Loop through the node's children/siblings
		for node, direction in get_children(current.x, current.y):
			#If it is already in the closed set, skip it
			if node in closedset:
				continue

			#Otherwise if it is already in the open set
			if node in openset:
				#Check if we beat the G score 
				new_g = current.G + 1
				if node.G > new_g:
					#If so, update the node to have a new parent
					node.G = new_g
					node.parent = current
					node.direction = direction
			else:
				#If it isn't in the open set, calculate the G and H score for the node
				node.G = current.G + 1
				node.H = pythagorean(node, end)

				#Set the parent to our current item
				node.parent = current
				node.direction = direction
				#Add it to the set
				openset.add(node)

	#Throw an exception if there is no path
	raise ValueError('No Path Found')





def bfs_clusters(start, clusters, cells, center = False):
	"""
	bfs_clusters takes start, dict of clusters, 
	set of cells (the graph), then finds the shortest path between start 
	and EVERY SINGLE CLUSTER

	cluster is dictionary of dictionaries. After exectution of the function 
	start_point has a path to every single cluster and vice versa. 
	
	the result path is a sequence of PAIRS (x, y) !

	:param start_point: (x0, y0):
	:param cells: {(x1, y1), (x2, y2), ...}:
	:param clusters: {cluster1 : None, clutser2 : None}:
	:param center = True is Center to Clusters:
	:param center = False is path Between every single cluster: 
	""" 

	count = 0 #countis number of clusters found

	visited = {start : "start"}
	
	q = deque([start])


	while q:
		x, y = q.popleft()
		for next_point in [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]:
			if (next_point in cells) and (next_point not in visited):
				visited[next_point] = (x,y)
				
				if next_point in clusters:
					count += 1

					path = [list(next_point)]
					prev_point = visited[next_point]
					while visited[prev_point] != "start":
						path.append(list(prev_point))
						prev_point = visited[prev_point]

					path.append(list(prev_point))


					if center:
						clusters[next_point] = path
						if count == len(clusters):
							return
					else:
						clusters[start][next_point] = path[::-1]
						clusters[next_point][start] = path

						#If all clusters are connected
						if count == len(clusters) - 1:
							return 
				q.append(next_point)

	raise ValueError('No Path Found')


def find_beacon(start, clusters, cells, limit = None):
	"""

	"""
	if start in clusters:
		return ["", start]
	used = dict()
	used[start] = [None, "s"]
	
	q = deque()
	q.append(start)
	
	counter = 0
	while q:
		x, y = q.popleft()
		for nx, ny, direction in [(x, y-1, "L"), (x, y+1, "R"), (x-1, y, "U"), (x+1,y, "D")]:
			next_cell = (nx, ny)
			counter += 1
			if counter > limit:
				
				return [None, None]
			
			if next_cell in cells and next_cell not in used:
				used[next_cell] = [(x, y), direction]
				q.append(next_cell)
				
				#
				if next_cell in clusters:
					backtrack = next_cell
					path = ""
					while used[backtrack][1] != "s":
	
						path += used[backtrack][1]
						backtrack = used[backtrack][0]
					
					return [path[::-1], next_cell]
	print(counter)
	raise ValueError('No Path Found')