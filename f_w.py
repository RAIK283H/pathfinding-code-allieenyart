import math 

def adjacency_list_to_matrix(graph_data):
    matrix = [[math.inf] * len(graph_data) for i in range (len(graph_data))]
    
    for i in range(len(graph_data)):
        for j in range(len(graph_data)):
            if j in graph_data[i][1]:
                matrix[i][j] = math.sqrt((graph_data[i][0][0] - graph_data[j][0][0])  ** 2 + (graph_data[i][0][1] - graph_data[j][0][1])  ** 2)

    return matrix

def floyd_warshall(graph_data):

    dist = adjacency_list_to_matrix(graph_data)
        
    parent = [[None] * len(graph_data) for i in range (len(graph_data))]

    for k in range(len(graph_data)):  
        for i in range(len(graph_data)):  
            for j in range(len(graph_data)):  
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = k

    return dist, parent

def floyd_warshall_path(parent, i, j):
    path = []
    z = parent[i][j]
    while z is not None:
        path.append(z)
        z = parent[i][z]
    path.append(i)
    path.reverse()
    path.append(j)
    return path

