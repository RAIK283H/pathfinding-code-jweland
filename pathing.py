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
    start_node = 0
    current_node = start_node
    last_node = (len(graph_data.graph_data[global_game_data.current_graph_index]) - 1)
    target = global_game_data.target_node[global_game_data.current_graph_index]
    destination = target
    path = []
    previous_node = None

    # Pre Conditions
    assert len(path) == 0, "Starting path needs to be empty"
    assert last_node != 0, "Ending node is not first node"
    assert start_node < target < last_node, "Target node is before last node and after start node"

    while(current_node != destination):
        neighbors = graph_data.graph_data[global_game_data.current_graph_index][current_node][1]

        if previous_node in neighbors and len(neighbors) > 1:
            neighbors.remove(previous_node)
        
        next_node = random.choice(neighbors)
        path.append(int(next_node))

        previous_node = current_node
        current_node = next_node

        if(current_node == target):
            destination = last_node

    # Post Conditions  
    assert len(path) > 0, "Path can not be empty" 
    assert current_node == last_node, "Ends with current node equals last node"

    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
