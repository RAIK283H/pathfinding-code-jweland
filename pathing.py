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
    # preconditions
    start_node = 0
    last_node = (len(graph_data.graph_data[global_game_data.current_graph_index]) - 1)
    current_node = start_node

    path = []

    while(current_node != last_node):
        neighbors = graph_data.graph_data[global_game_data.current_graph_index][current_node][1]
        next_node = random.choice(neighbors)
        path.append(int(next_node))
        current_node = next_node

    # post conditions
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
