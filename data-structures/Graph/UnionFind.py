'''
UnionFind implementation:
    - QuickFind
    - QuickUnion

- QuickUnion is more efficient than QuickFind in general.
- In QuickFind the root array stores the root of the node.
- In QuickUnion the root array stores the parent of the node.
- Root node's parent is node itself.
'''

# QuickFind
class UnionFindQF:
    # TC - O(n)
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    # TC - O(1)
    def find(self, x: int) -> int:
        return self.root[x]

    # TC - O(n)
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x

    # TC - O(1)
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# QuickUnion
class UnionFindQU:
    # TC - O(n)
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # TC - O(n)
    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x

    # TC - O(n)
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    # TC - O(n)
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    

# QuickUnion (Path Compression)
class UnionFindPathCompression:
    # TC - O(n)
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # TC - O(log(n))
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # TC - O(log(n))
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    # TC - O(log(n))
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# Union by rank
class UnionFindRanked:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # TC - O(log(n))
    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x

    # TC - O(log(n))
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    # TC - O(log(n))
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    

# UnionFind (PathCompression + union by rank)
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


if __name__ == "__main__":
    # Test Case
    uf = UnionFindQF(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true


    # Test Case
    uf = UnionFindQU(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true


    # Test Case
    uf = UnionFindPathCompression(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true


    # Test Case
    uf = UnionFindRanked(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true