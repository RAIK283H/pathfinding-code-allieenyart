from graph_data import graph_data
import permutation
import math

def main():
    valid_graphs = [graph_data[0], graph_data[1], graph_data[10], graph_data[11], graph_data[12]]
    print("Listing all valid hamiltonian cycles: ")
    for graph in valid_graphs:
        print("processing graph ", graph_data.index(graph), ":")
        cycles = permutation.find_hamiltonian_cycles(graph)
        # extra credit 
        
        if cycles != -1:
            smallest_distance = math.inf
            shortest_cycle = None

            for cycle in cycles:
                total_distance = path_distance(graph, cycle)
                if total_distance < smallest_distance:
                    smallest_distance = total_distance
                    shortest_cycle = cycle
            print("Shortest cycle: ", shortest_cycle)
        find_largest_clique(graph)

   
        
# distance helper function
def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# another distance helper function
def path_distance(graph, cycle):
    distance = 0
    for i in range(len(cycle) - 1):
        distance += calculate_distance(graph[cycle[i]][0], graph[cycle[i + 1]][0])
    return distance

# extra credit gets all subsets 
def generate_subsets(nodes, index=0, current_subset=None, all_subsets=None):
    if all_subsets is None:
        all_subsets = []
    if current_subset is None:
        current_subset = []

    # base case
    if index == len(nodes):
        all_subsets.append(list(current_subset))
        return all_subsets

    generate_subsets(nodes, index + 1, current_subset, all_subsets)

    current_subset.append(nodes[index])
    generate_subsets(nodes, index + 1, current_subset, all_subsets)
    current_subset.pop() 

    return all_subsets

# checks if a subset is a clique 
def is_clique(graph, subset):
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            node1 = subset[i]
            node2 = subset[j]
            if node2 not in graph[node1][1]: 
                return False
    return True

# finds and prints the largest clique
def find_largest_clique(graph):
    n = len(graph)
    if n <= 2:
        print("No cliques can be found with fewer than 3 nodes.")
        return []

    nodes = list(range(1, n - 1))  

    all_subsets = generate_subsets(nodes)
    largest_clique = []

    for subset in all_subsets:
        if is_clique(graph, subset) and len(subset) > len(largest_clique):
            largest_clique = subset

    print("Largest Clique:", largest_clique)
    return largest_clique



if __name__ == "__main__":
    main()