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

# gets a random path without letting the player exit without visiting the target
def get_random_path():
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
    graph = graph_data.graph_data[global_game_data.current_graph_index]

    # preconditions
    assert len(graph) > 1, "the length must be greater than one so theres a start and exit node"
    assert target_node != exit_node, "target node cannot be the same as the exit node"
    assert start_node == 0, "start node must be at index 0"

    path = [start_node]
    current_node = start_node

    while current_node != target_node:
        # randomly picks a neighbor node
        next_node = random.choice(graph[current_node][1]) 
        path.append(next_node)
        current_node = next_node

    while current_node != exit_node:
        # randomly picks a neighbor node
        next_node = random.choice(graph[current_node][1]) 
        path.append(next_node)
        current_node = next_node

    #postconditionss 
    assert path[0] == start_node, "path should start at the start "
    assert target_node in path, "path should visit the target"
    assert path[-1] == exit_node, "path should end at exit"

    return path

    


def get_dfs_path():  
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
