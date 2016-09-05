from graph import Graph

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

stage0_edges = []

for j,row in enumerate(stage0):
    stage0_edges.append([])
    for i,col in enumerate(stage0[j]):
        if stage0[j][i] in [1,2,6]:
            stage0_edges[j].append(get_neighbors(stage0,j,i))
        else:
            stage0_edges[j].append(0)

stage0_heuristics = calculate_heuristics(stage0, (0, 0))
movement_cost  = 10 # G in A* algorithm

g = Graph()

for j,row in enumerate(stage0):
    for i,col in enumerate(stage0[j]):
        if stage0[j][i] in [1,2,6]:
            g.add_vertex((j, i), stage0_heuristics[j][i])
            map(lambda n: g.add_edge((j, i), n), get_neighbors(stage0, j, i)) #wordy, but basically for each neighbor return in get_neighbors, we add it as an edge using add_edge method of the graph object

#use priority queue to keep track of lowest F cost; F = G+H
#import ipdb; ipdb.set_trace()
