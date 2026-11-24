def bellman_ford(graph, src, dest):
    distances = dict()
    for node in graph:
        distances[node] = float("inf")
    distances[src] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                relax_edge(distances, u, v, w)

    for u in graph:
        for v, w in graph[u].items():
            if relax_edge(distances, u, v, w):
                raise Exception("negative cycle detected!")

    return distances[dest]

def relax_edge(distances, node1, node2, weight_1_2):
    if distances[node1] + weight_1_2 < distances[node2]:
        distances[node2] = distances[node1] + weight_1_2
        return True

    return False
