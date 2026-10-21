import time

# Graph
graph = {
    'A': ['B', 'C', 'F'],
    'B': ['D'],
    'C': ['E'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


# BFS Algorithm
def bfs(start, goal):
    queue = [start]
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


# DFS Algorithm
def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# Run BFS
start_time = time.perf_counter()
bfs_nodes = bfs('A', 'G')
bfs_time = (time.perf_counter() - start_time) * 1000


# Run DFS
start_time = time.perf_counter()
dfs_nodes = dfs('A', 'G')
dfs_time = (time.perf_counter() - start_time) * 1000


# Display results
print("====================================")
print("       BFS vs DFS Profiling")
print("====================================")

print("\nBFS Results:")
print("Nodes Expanded:", bfs_nodes)
print("Execution Time: {:.6f} ms".format(bfs_time))

print("\nDFS Results:")
print("Nodes Expanded:", dfs_nodes)
print("Execution Time: {:.6f} ms".format(dfs_time))
ha mala github cha code aahe tyat redmi and ai construbustioon de mala takayla
