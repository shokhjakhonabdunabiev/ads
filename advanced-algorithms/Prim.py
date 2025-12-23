from collections import defaultdict
import heapq

def minimumSpanningTree(edges: list[list[int]], n: int):
    adj = defaultdict(list)
    for src, dst, weight in edges:
        adj[src].append([dst, weight])
        adj[dst].append([src, weight])
    
    min_heap = []
    for neighbor, weight in adj[1]:
        heapq.heappush(min_heap, [weight, 1, neighbor])
    
    mst = []
    visited = set()
    visited.add(1)
    while min_heap:
        weight, src, node = heapq.heappop(min_heap)
        if node in visited:
            continue
            
        mst.append([src, node])
        visited.add(node)
        for neighbor, weight in adj[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, [weight, node, neighbor])
    return mst