# Depth First Search (DFS) Implementation

def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            # Add neighbors in reverse order to match sample output
            stack.extend(reversed([nbr for nbr in graph[node] if nbr not in visited]))

    return traversal


# Driver code
if __name__ == "__main__":
    n, e = map(int, input().split())
    graph = {}

    for _ in range(e):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Start DFS from the first node given in the first edge
    start_node = list(graph.keys())[0]

    result = dfs(graph, start_node)
    print(result)   