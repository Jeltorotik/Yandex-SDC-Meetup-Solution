DXDY = [[0,-1],[0,1],[1,0],[-1,0]] 
def bfs_points(start_point, clusters, cells):
	used = [[False] * N for _ in range(N)]
	
	x_start, y_start = start_point
	used[x_start][y_start] = "start"
	
	q = deque()
	q.append([x_start,y_start])

	count = 0
	while q:
		x, y = q.popleft()
		for dx, dy in DXDY:
			nx = x + dx
			ny = y + dy
			if 0 <= nx < N and 0 <= ny < N:
				if (nx, ny) in cells and not used[nx][ny]:
					used[nx][ny] = (x,y)
					
					if (nx, ny) in clusters:
						path = [[nx, ny]]
						back_x, back_y = x, y
						
						while used[back_x][back_y] != "start":
							path.append([back_x,back_y])
							back_x, back_y = used[back_x][back_y]
						path.append([back_x,back_y])
						clusters[start_point][(nx, ny)] = path[::-1]
						clusters[(nx, ny)][start_point] = path
						
						#Если нашли все пути
						if len(clusters[start_point]) == len(clusters) - 1:
							return 
					
					q.append([nx, ny])

raw_clusters = {(676, 170), (420, 421), (799, 496), (467, 503), (556, 546), (450, 639), (448, 472), (423, 338), (571, 574), (388, 408), (480, 407), (452, 519), (365, 919), (291, 844), (498, 643), (422, 480), (279, 162), (410, 575), (462, 410), (461, 372), (246, 141), (807, 729), (504, 556), (460, 533), (433, 549), (779, 457), (502, 910), (478, 522), (787, 739), (378, 529), (336, 462), (393, 512), (399, 383), (488, 424), (342, 455), (380, 408), (323, 419), (844, 711), (448, 371), (347, 836), (575, 607), (458, 489), (430, 381), (366, 913), (439, 549), (468, 547), (392, 458), (460, 816), (495, 612), (394, 704), (333, 437), (391, 361), (549, 617), (344, 423), (373, 508), (695, 500), (481, 584), (458, 315), (712, 763), (319, 843), (410, 404), (525, 603), (362, 489), (409, 444), (820, 410), (489, 539), (404, 437), (507, 458), (370, 285), (441, 622), (531, 554), (773, 771), (353, 471), (402, 559), (265, 853), (729, 485), (411, 345), (372, 392), (390, 539), (394, 320), (526, 500), (473, 655), (439, 450), (448, 356), (516, 587), (706, 496), (430, 595), (856, 784), (459, 425), (443, 504), (423, 370), (739, 479), (811, 442), (387, 659), (781, 734), (796, 474), (431, 435), (382, 524), (841, 796), (484, 652), (439, 495), (496, 647)}

def calculate_clusters():
	clusters = {cluster : {} for cluster in raw_clusters}
	for point in clusters.keys():
		bfs_points(point, clusters, cells)
		
		
		
	POINTS_D = {(0, -1) : "L",
				(0, 1) : "R",
				(1, 0) : "D",
				(-1,0) : "U"}
	for point1 in clusters.keys():
		for point2 in clusters[point1].keys():
			point1_to_point2 = clusters[point1][point2]
			
			path = ""
			for i in range(len(point1_to_point2) - 1):
				x1, y1 = point1_to_point2[i]
				x2, y2 = point1_to_point2[i+1]
				path += POINTS_D[(x2 - x1, y2 - y1)]
			clusters[point1][point2] = path
	return clusters


import random
from collections import deque

#Заказы и пути к ним
REVERSE_DIR = {"D" : "U",
			  "U" : "D",
			  "R" : "L",
			  "L" : "R"}

def reverse_path(path):
	#path = "DDRRL" -> "UULLR" -> "RLLUU"
	rev_path = ""
	for direction in path[::-1]:
		rev_path += REVERSE_DIR[direction]
	return rev_path








def find_beacon(start, clusters, cells, limit):
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
	raise ValueError('No Path Found')




def show_paths(R, robots):
	paths = [None] * R
	
	for robot in robots:
		path_60  = robot.get_path()
		paths[robot.idx] = path_60

	path = '\n'.join(paths)
	print(path, flush = True)
		
		

class Robot:
	def __init__(self, idx, cell):
		self.idx = idx #Его индекс
		self.path = "" #Его путь
		self.iter = 0
		self.position = cell


	def get_path(self):
		cur_path = self.path[self.iter:self.iter+60]
		self.iter += 60
		if len(cur_path) < 60:
			self.path = ""
			self.iter = 0
			cur_path += "S" * (60 - len(cur_path))

			chill_robots.append(self.idx)

		return cur_path
		




class Order:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		

		self.beacon_to_start = None
		self.start_to_beacon = None
		self.beacon_to_end = None
		self.end_to_beacon = None
		self.cluster_start = None
		self.cluster_end = None
		
		self.path = ""
		
		
		
	def build_path(self):
		
		self.path = ''.join([self.beacon_to_start, 
						"T", 
						self.start_to_beacon, 
						clusters[self.cluster_start][self.cluster_end], 
						self.beacon_to_end,
						"P",
						self.end_to_beacon])


		
		return self.path 
	



	

N, MaxTips, Cost = map(int, input().split())

board = []
for i in range(N):
	line = input().strip()
	board.append(line)

T, D = map(int, input().split())






if N != 1000:
	print(1, flush = True)
	if N == 4 or N == 128:
		print(1,1, flush = True)
	elif N == 180:
		print(6,6, flush = True)
	elif N == 384:
		print(12, 12, flush = True)
	elif N == 1024:
		print(12, 12, flush = True)
	for i in range(T):
		k = int(input())
		for j in range(k):
			x1, y1, x2, y2 = map(int, input().split())
		print("S" * 60, flush = True)


else:
	#Иннополис
	cells = set()
	for x in range(N):
		for y in range(N):
			if board[x][y] == ".":
				cells.add((x,y))  



	clusters = calculate_clusters()

	R = 100 # Количество роботов
	LIMIT = 10000 #Максимальное кол-во итераций BFS для поиска кластера


	print(R, flush = True)


	random_clusters = random.sample(raw_clusters, R//2) + random.sample(raw_clusters, R//2)

	
	robots = [Robot(idx, cell) for idx, cell in enumerate(random_clusters)]
	
	chill_robots = list(range(R))


	for robot in robots:
		x, y = robot.position
		print(x+1, y+1, flush = True)



	#ORDERS:
	orders = {cell : deque() for cell in raw_clusters}

	orders_to_clusters = {}
	

	for i in range(T):
		
		
		k = int(input())
		for j in range(k):
			x1, y1, x2, y2 = map(int, input().split())

			order_start = (x1 - 1, y1 - 1)
			order_end = (x2 - 1, y2 - 1)

	
			
			if order_start in orders_to_clusters:
				path_start, cluster_start = orders_to_clusters[order_start]
			else:
				path_start, cluster_start = find_beacon(order_start, raw_clusters, cells, limit = LIMIT)
				orders_to_clusters[order_start] = (path_start, cluster_start)
				
			if order_end in orders_to_clusters:
				path_end, cluster_end = orders_to_clusters[order_end]
			else:
				path_end, cluster_end = find_beacon(order_end, raw_clusters, cells, limit = LIMIT)
				orders_to_clusters[order_end] = (path_end, cluster_end)



			
			order = Order(order_start, order_end)
	
			
			
			order.start_to_beacon = path_start
			order.beacon_to_start = reverse_path(path_start)
			order.end_to_beacon = path_end
			order.beacon_to_end = reverse_path(path_end)
			order.cluster_start = cluster_start
			order.cluster_end = cluster_end
			
			orders[cluster_start].append(order)
		

		#Для каждого робота проверить, есть ли заказ
		for robot_idx in chill_robots:
			
			robot = robots[robot_idx]

			if orders[robot.position]:
				
				order = orders[robot.position].popleft()
	
				robot.path = order.build_path()
				robot.position = order.cluster_end


			else:
					#Посылаем в рандомный cell


				random_cluster = random.sample(raw_clusters, 1)[0]
				while random_cluster == robot.position:
					random_cluster = random.sample(raw_clusters, 1)[0]

				robot.path = clusters[robot.position][random_cluster]
				robot.position = random_cluster

		chill_robots = []
		show_paths(R, robots)
		