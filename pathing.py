import graph_data
import global_game_data
from numpy import random
from collections import deque
import heapq
import math

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    # More up here
    assert graph_data.graph_data is not None, "Graph does not exist"
    assert global_game_data.target_node[global_game_data.current_graph_index] is not None, "Target does not exist"
    assert len(graph_data.graph_data[global_game_data.current_graph_index]) > 0, "Graph data is not empty"

    start_node = 0
    current_node = start_node
    last_node = (len(graph_data.graph_data[global_game_data.current_graph_index]) - 1)
    target = global_game_data.target_node[global_game_data.current_graph_index]
    destination = target
    path = []

    while(current_node != destination):
        # Creates the neighbors list
        neighbors = graph_data.graph_data[global_game_data.current_graph_index][current_node][1]

        if start_node in neighbors:
            neighbors.remove(start_node)

        #Gets next node from neighbors list
        next_node = random.choice(neighbors)
        path.append(int(next_node))

        current_node = next_node

        if(current_node == target):
            destination = last_node

    # Post Conditions  
    assert check_path(graph_data.graph_data[int(global_game_data.current_graph_index)], path), "Not valid path"
    assert start_node == 0, "The path started at 0 (the start node)"
    assert len(path) > 0, "Path can not be empty" 
    assert target in path, "Path needs to hit the target"
    assert current_node == last_node, "Ends with current node equals last node"


    return path


def get_dfs_path():
    start_node = 0
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    last_node = (len(graph) - 1)

    # to get paths for path to target and end to target
    path_to_target = dfs(graph, start_node, target)
    path_to_end = dfs(graph, target, last_node)

    # create the path
    path = path_to_target[1:] + path_to_end[1:]

    # post conditions
    assert check_path(graph_data.graph_data[int(global_game_data.current_graph_index)], path), "Not valid path"
    assert target in path, "Path needs to hit the target"
    assert last_node in path, "Path needs to hit the last node"

    return path

# dfs function call
def dfs(graph, start, end):
    visited = set()
    stack = [start]
    parent = {start: None}

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            if node == end:
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]
            
            neighbors = graph[node][1]

            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    parent[neighbor] = node 

    return None 

def get_bfs_path():
    start_node = 0
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    last_node = (len(graph) - 1)
    
    # to get paths for path to target and end to target
    path_to_target = bfs(graph, start_node, target)
    path_to_end = bfs(graph, target, last_node)

    # create the path
    path = path_to_target[1:] + path_to_end[1:]

    # post conditions
    assert check_path(graph_data.graph_data[int(global_game_data.current_graph_index)], path), "Not valid path"
    assert target in path, "Path needs to hit the target"
    assert last_node in path, "Path needs to hit the last node"
    return path

# main call for bfs
def bfs(graph, start, end):
    visited = set()
    queue = deque([start])
    parent = {start: None}
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        if node not in visited:
            visited.add(node)
            
            neighbors = graph[node][1]
            
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in parent:
                    queue.append(neighbor)
                    parent[neighbor] = node

    return None

class Node:
    def __init__(self, id, distance=float('inf'), parent=None):
        self.id = id
        self.distance = distance
        self.parent = parent

    def __lt__(self, other):
        return self.distance < other.distance

def euclidean_distance(coord1, coord2):
    return math.sqrt(math.pow((coord1[0] - coord2[0]),2) + math.pow((coord1[1] - coord2[1]),2))

def dijkstra_path(graph, start, end):
    # setup all the distance and parent variables
    distances = {i: float('inf') for i in range(len(graph))}
    distances[start] = 0
    priority_queue = []
    heapq.heappush(priority_queue, Node(start, distance=0))
    parents = {start: None}

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        # if target/node is hit
        if current_node.id == end:
            # build the path
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parents.get(current)
            path.reverse()
            return path

        current_coord, neighbors = graph[current_node.id][0], graph[current_node.id][1]

        # check the distance of each neighbor
        for neighbor in neighbors:
            neighbor_coord = graph[neighbor][0]
            weight = euclidean_distance(current_coord, neighbor_coord)
            new_distance = current_node.distance + weight

            # update the path if shorter
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = current_node.id
                heapq.heappush(priority_queue, Node(neighbor, new_distance))

    return None

def get_dijkstra_path():
    start_node = 0
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    last_node = len(graph) - 1

    # run dijkstra on graph
    start_to_target = dijkstra_path(graph, start_node, target)
    target_to_end = dijkstra_path(graph, target, last_node)
    final_path = start_to_target[1:-1] + target_to_end

    # return the path
    assert start_to_target[0] == start_node, "Path is started at the start node"
    assert final_path[len(final_path) - 1] == last_node, "Path is ended on the last node"
    assert check_path(graph, final_path), "Path is connected"
    return final_path


def check_path(graph, path):
    for i in range(len(path) - 1):
        if path[i+1] not in graph[path[i]][1]:
            return False
    
    return True