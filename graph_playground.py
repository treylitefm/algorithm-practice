from graph import Graph
from priority_queue2 import PriorityQueue

def get_neighbors(grid, y, x): #TODO: delete
    neighbors = []
    if y+1 < len(grid) and grid[y+1][x] in [1,6,2]:
        neighbors.append((y+1,x))
    if y-1 >= 0 and grid[y-1][x] in [1,6,2]:
        neighbors.append((y-1,x))
    if x+1 < len(grid[y]) and grid[y][x+1] in [1,6,2]:
        neighbors.append((y,x+1))
    if x-1 >= 0 and grid[y][x-1] in [1,6,2]:
        neighbors.append((y,x-1))
    return neighbors

def get_manhattan_distance(point1, point2): #expected tuples
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

def calculate_heuristics(grid, origin):
    heuristics = []
    for j,row in enumerate(grid):
        heuristics.append([])
        for i,col in enumerate(grid[j]):
            if grid[j][i] in [1,2,6]:
                heuristics[j].append(get_manhattan_distance((j,i),origin))
            else:
                heuristics[j].append(0)
    return heuristics

def calculate_f_cost(g, vertex_dest, vertex_origin_movement_cost): #need origin and dest because G (movement cost) can change depending on where you're coming from
    return vertex_origin_movement_cost + 10 + g.get_vertex_value(vertex_dest) #G+H

stage0 = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],

        [0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],
        [0,2,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,2,0],
        [0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],

        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],

        [0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0],

        [0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0],

        [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,6,6,6,6,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,6,6,6,6,0],
        [0,6,6,6,6,0,1,0,0,6,6,6,6,6,6,6,6,6,6,0,0,1,0,6,6,6,6,0],
        [0,6,6,6,6,0,1,0,0,6,0,0,0,0,0,0,0,0,6,0,0,1,0,6,6,6,6,0],
        [0,0,0,0,0,0,1,0,0,6,0,6,6,6,6,6,6,0,6,0,0,1,0,0,0,0,0,0],

        [5,6,6,6,6,6,1,6,6,6,0,6,6,6,6,6,6,0,6,6,6,1,6,6,6,6,6,5],

        [0,0,0,0,0,0,1,0,0,6,0,6,6,6,6,6,6,0,6,0,0,1,0,0,0,0,0,0],
        [0,6,6,6,6,0,1,0,0,6,0,0,0,0,0,0,0,0,6,0,0,1,0,6,6,6,6,0],
        [0,6,6,6,6,0,1,0,0,6,6,6,6,6,6,6,6,6,6,0,0,1,0,6,6,6,6,0],
        [0,6,6,6,6,0,1,0,0,6,0,0,0,0,0,0,0,0,6,0,0,1,0,6,6,6,6,0],
        [0,0,0,0,0,0,1,0,0,6,0,0,0,0,0,0,0,0,6,0,0,1,0,0,0,0,0,0],

        [0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],

        [0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],

        [0,2,1,1,0,0,1,1,1,1,1,1,1,6,6,1,1,1,1,1,1,1,0,0,1,1,2,0],

        [0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
        [0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],

        [0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],

        [0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],

        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]

origin = (1, 1)
destination = (5, 5)

stage0_edges = []

for j,row in enumerate(stage0):
    stage0_edges.append([])
    for i,col in enumerate(stage0[j]):
        if stage0[j][i] in [1,2,6]:
            stage0_edges[j].append(get_neighbors(stage0,j,i))
        else:
            stage0_edges[j].append(0)

stage0_heuristics = calculate_heuristics(stage0, origin)

g = Graph()

#add calculated heuristics to graph
for j,row in enumerate(stage0):
    for i,col in enumerate(stage0[j]):
        if stage0[j][i] in [1,2,6]:
            g.add_vertex((j, i), stage0_heuristics[j][i])
            map(lambda n: g.add_edge((j, i), n), get_neighbors(stage0, j, i)) #wordy, but basically for each neighbor return in get_neighbors, we add it as an edge using add_edge method of the graph object

movement_costs = { 0: origin }#keep all movement costs outside of graph because its easier to update; key is the f cost, value is composed of all vertices that map to a particular f cost
vertex = origin
pq = PriorityQueue([])

while True: #shall we tackle bfs with recursion? :(
    if vertex is destination:
        break
    for neighbor in get_neighbors(vertex):
        f_cost = calculate_f_cost(g, neighbor, vertex_f_cost - g.get_vertex_value(vertex)) #gross and cryptic; TODO: refactor once it works
        pq.push(f_cost)
        if movement_costs[f_cost] is None: movement_costs[f_cost] = []
        movement_costs[f_cost].append(neighbor)
    vertex_f_cost = pq.pop()
    vertex = movement_costs[vertex_f_cost].pop() #gross and cryptic; TODO: refactor once it works


#use priority queue to keep track of lowest F cost; F = G+H
#import ipdb; ipdb.set_trace()
