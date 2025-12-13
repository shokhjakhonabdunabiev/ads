'''
Kahn's Algorithm - Topological Sort

What Kahn's Algorithm Does
- Computes a topological order of nodes in a directed graph
- Detects cycles (if a topological order is impossible)
'''

from collections import defaultdict, deque

# TC - O(n + m)
def topological_sort(vertices: list[int], edges: list[(int, int)]) -> list[int]:
    adj = defaultdict(list)
    in_degree = {v: 0 for v in vertices}

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == len(vertices):
        return topo_order

    return None


if __name__ == "__main__":
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [
        (5, 2),
        (5, 0),
        (4, 0),
        (4, 1),
        (2, 3),
        (3, 1)
    ]

    result = topological_sort(vertices, edges)

    if result is None:
        print("Cycle detected — topological sort not possible.")
    else:
        print("Topological Order:", result)
