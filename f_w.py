from graph_data import graph_data
import math



def adjacency_to_matrix(graph):
    n = len(graph)
    
    matrix = [[float('inf')] * n for i in range(n)]

    for i in range(n):
        matrix[i][i] = 0
    
    for i in range(len(graph)):
        neighbors = graph[i][1] 
        for neighbor in neighbors:
            coord1 = graph[i][0]
            coord2 = graph[neighbor][0]
            distance = math.sqrt(pow((coord2[0] - coord1[0]),2) + pow((coord2[1] - coord1[1]),2))
            matrix[i][neighbor] = round(distance, 2)
    return matrix

def create_parent_graph(n):
    return [[None for i in range(n)] for i in range(n)]



def floyd_warshall(matrix):
    n = len(matrix)
    parent = create_parent_graph(n)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parent[i][j] = k
    return matrix, parent

def floyd_warshall_path(P, i, j):
    if P[i][j] is None:
        return None

    path = []
    z = P[i][j]
    while z is not None:
        path.insert(0, z)
        z = P[i][z]
    path.insert(0, i)
    path.append(j) 
    return path




if __name__ == "__main__":
    graph = graph_data[0]
    matrix = adjacency_to_matrix(graph)
    distances, parent = floyd_warshall(matrix)
    path = floyd_warshall_path(parent, 0, 2)

    print("Matrix:")
    for row in distances:
        print(row)

    print("Path:")
    print(path)