import math

def sjt_permutations(graph):
    # get length of graph
    n = len(graph)
    if n == 0:
        return []
    # create perm
    perms = list(range(n))
    # create directions field
    directions = [-1] * n 
    # add first perm
    permutations = [perms[:]]

    # helper function to get mobile
    def get_mobile():
        mobile = -1
        index = -1
        for i in range(n):
            neighbor = i + directions[i]
            if 0 <= neighbor < n and perms[i] > perms[neighbor] and (mobile == -1 or perms[i] > perms[index]):
                mobile = perms[i]
                index = i
        return index

    while True:
        index = get_mobile()
        if index == -1:
            break

        neighbor = index + directions[index]

        # swaps
        temp = perms[index]
        perms[index] = perms[neighbor]
        perms[neighbor] = temp

        temp = directions[index]
        directions[index] = directions[neighbor]
        directions[neighbor] = temp

        temp = index
        index = neighbor
        neighbor = temp


        # change directions
        for i in range(n):
            if perms[i] > perms[index]:
                directions[i] = -directions[i]

        # add new perm to the list
        permutations.append(perms[:])

    return permutations

def find_hamilition_cycles(graph, permutations):
    valid = []
    # find the cycles
    for cycle in permutations:
        full_cycle = cycle + [cycle[0]]
        if is_valid_hamilition(graph, full_cycle):
            valid.append(full_cycle)

    return valid

def is_valid_hamilition(graph, cycle):
    # checks with neighbor to determine valid cycle
    for i in range(len(cycle) - 1):
        if cycle[i+1] not in graph[cycle[i]][1]:
            return False 
    return True

def calculate_cycle_distance(graph, cycle):
    # calculates the distance between each node in perm
    total_distance = 0
    for i in range(len(cycle) - 1):
        coord1 = graph[cycle[i]][0]
        coord2 = graph[cycle[i + 1]][0]
        distance = math.sqrt(pow((coord2[0] - coord1[0]),2) + pow((coord2[1] - coord1[1]),2))
        total_distance += distance
    return total_distance

def find_optimal_ham_cycles(valid_cycles, graph):
    min_distance = float('inf')
    optimal_cycles = []
    
    # finds the best cycle(s)
    for cycle in valid_cycles:
        cycle_distance = calculate_cycle_distance(graph, cycle)
        if cycle_distance < min_distance:
            min_distance = cycle_distance
            optimal_cycles = [cycle]
        elif cycle_distance == min_distance:
            optimal_cycles.append(cycle)

    return optimal_cycles