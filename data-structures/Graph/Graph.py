'''
Graph
'''
from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.adj = dict()
        self.directed = directed

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u, v, weight=1):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def remove_edge(self, u, v):
        if u in self.adj:
            self.adj[u] = [(n, w) for (n, w) in self.adj[u] if n != v]

        if not self.directed and v in self.adj:
            self.adj[v] = [(n, w) for (n, w) in self.adj[v] if n != u]

    def remove_node(self, node):
        for u in list(self.adj):
            self.adj[u] = [(v, w) for (v, w) in self.adj[u] if v != node]
        if node in self.adj:
            del self.adj[node]

    def neighbors(self, node):
        return self.adj.get(node, [])

    def __repr__(self):
        return "\n".join(f"{u}: {self.adj[u]}" for u in self.adj)
    

def bfs(graph: Graph, start):
    res = []
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node in visited:
            continue
        res.append(node)
        for neigh in graph.neighbors(node):
            q.append(neigh)
    return res

def dfs(graph: Graph, start, visited=set(), res=[]):
    if start in visited:
        return
    visited.add(start)
    res.append(start)
    for neigh in graph.neighbors(start):
        dfs(graph, neigh, visited, res)