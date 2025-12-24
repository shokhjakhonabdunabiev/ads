import heapq

class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def minimumSpanningTree(edges: list[list[int]], n: int) -> list[list[int]]:
    min_heap = []
    for n1, n2, weight in edges:
        heapq.heappush(min_heap, [weight, n1, n2])

    uf = UnionFind(n)
    mst = []
    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(min_heap)
        if not uf.connected(n1, n2):
            uf.union(n1, n2)
            mst.append([n1, n2])
    return mst