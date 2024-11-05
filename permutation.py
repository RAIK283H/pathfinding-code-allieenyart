import math

# sjt implemented from psuedocode
going_left = True
going_right = False

# gets the greatest mobile
def find_largest_mobile(array, dir, n):
    assert len(array) == n, "array length should be n"
    mobile = 0
    for i in range (n):
        if dir[array[i] - 1 ] == going_left and i > 0:
            if array[i] > array[i-1] and array[i] > mobile:
                mobile = array[i]
        elif dir[array[i] - 1 ] == going_right and i < n - 1:
            if array[i] > array[i + 1] and array[i] > mobile:
                mobile = array[i]
    assert mobile >= 0, "mobile value cant be negative"
    return mobile
        
# gets one permutation
def get_one_perm (array, dir, n):
    assert len(array) == n, "array length should be n"
    mobile = find_largest_mobile(array, dir, n)

    if mobile == 0:
        return
    pos = array.index(mobile)

    # swap according to the direction 
    if dir[mobile - 1] == going_left:
        array[pos], array[pos - 1] = array[pos - 1], array[pos]
        pos -= 1
    elif dir[mobile - 1] == going_right:
        array[pos], array[pos + 1] = array[pos + 1], array[pos]
        pos += 1

    # change direction for elts greater than largest mobile
    for i in range (0 , n):
        if array[i] > mobile:
            dir[array[i] - 1] = not dir[array[i] - 1]

    perm = []
    for i in range(n): 
        perm.append(array[i])
    assert len(perm) == n, "perm should be length n"
    return perm


# gets all permutations of natural numbers through n
def get_perms_sjt(n):
    assert n > 0, "n should be a natural number"
    array = [i + 1 for i in range (0, n)]

    perms = []
    first_perm = []
    for i in range(n): 
        first_perm.append(array[i])
    perms.append(first_perm)
    
    dir = [going_left for _ in range (n)]

    for i in range (1, math.factorial(n)):
        perms.append(get_one_perm(array, dir, n))

    assert len(perms) == math.factorial(n), "there should be n factorial permutations"
    return perms

def is_hamiltonian_cycle(graph, path):
    assert path != None, "path shouldn't be none"
    # check if the path is a valid cycle
    for i in range(1, len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        if next_node not in graph[current_node][1]:
            return False
    
    assert path[0] == path[-1], "path should start and end at the same node"
    return True

def find_hamiltonian_cycles(graph):
    assert graph != None, "graph can't be none"
    n = len(graph)
    valid_cycles = []

    # no valid cycles
    if n <= 2:
        print("-1")
        return -1
    
    for perm in get_perms_sjt(n-2):
        cycle = perm + [perm[0]]
        if is_hamiltonian_cycle(graph, cycle):
            valid_cycles.append(cycle)

    assert all(is_hamiltonian_cycle(graph, cycle) for cycle in valid_cycles), "all cycles should be valid hamiltonian cycles"
    print(valid_cycles)
    return valid_cycles
