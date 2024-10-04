import graph_data
import global_game_data
from numpy import random

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
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]

def check_path(graph, path):
    for i in range(len(path) - 1):
        if path[i+1] not in graph[path[i]][1]:
            return False
    
    return True