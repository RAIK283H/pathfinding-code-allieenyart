import graph_data
import global_game_data
from collections import deque
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

    
def dfs(graph, start, target):
    stack = [(start, [start])]  
    visited = set()

    # go look at all nodes on the stack and add to a set of visited nodes when we visit them
    while stack:
        (node, path) = stack.pop()

        if node not in visited:
            if node == target:
                # all done!
                return path
            
            visited.add(node)
            # iterate over neighbors
            for neighbor in graph[node][1]: 
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))


       
    # return nothing if there is no path to the target
    return []  

def get_dfs_path():  
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    
    path_to_target = dfs(graph, start_node, target_node)
    
    path_to_exit = dfs(graph, target_node, exit_node)

    # add together
    full_path = path_to_target + path_to_exit[1:]

     # postconditions
    assert target_node in full_path, "the target node wasn't in the full path"
    assert full_path[-1] == exit_node, "the last node wasn't the exit node"

    for i in range(len(full_path) - 1):
        current_node = full_path[i]
        next_node = full_path[i + 1]
        assert next_node in graph[current_node][1], "there wasn't an edge connecting sequential vertices at some place in this path"
    
    return full_path

def bfs(graph, start, target):
    queue = deque([(start, [start])])
    visited = set()

    # search em all to find the shortest path
    while queue:
        (node, path) = queue.popleft()

        if node in visited:
            continue
        visited.add(node)

        if node == target:
            return path 

        for neighbor in graph[node][1]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # return nothing if there is no path to the target
    return []  

def get_bfs_path():
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    
    path_to_target = bfs(graph, start_node, target_node)
    
    path_to_exit = bfs(graph, target_node, exit_node)
    
    # add together
    full_path = path_to_target + path_to_exit[1:]

    # postconditions
    assert target_node in full_path, "the target node wasn't in the full path"
    assert full_path[-1] == exit_node, "the last node wasn't the exit node"

    for i in range(len(full_path) - 1):
        current_node = full_path[i]
        next_node = full_path[i + 1]
        assert next_node in graph[current_node][1], "there wasn't an edge connecting sequential vertices at some place in this path"

    return full_path


def get_dijkstra_path():
    return [1,2]
