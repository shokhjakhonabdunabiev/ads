'''
Binary Search Tree (BST)
'''

from collections import deque

class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"        

class BSTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val: int):        
        def dfs(node: Node):
            if node is None:
                return Node(val)
            if val <= node.val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            return node
        self.root = dfs(self.root)

    def delete(self, val: int):
        def dfs(node: Node, val: int):
            if node is None:
                return None
            if val < node.val:
                node.left = dfs(node.left, val)
            elif val > node.val:
                node.right = dfs(node.right, val)
            else:
                if not (node.left or node.right):
                    node = None
                elif node.right:
                    node.val = self.successor(node)
                    node.right = self.dfs(node.right, node.val)
                else:
                    node.val = self.predecessor(node)
                    node.left = self.dfs(node.left, node.val)
            return node
        dfs(self.root)
    
    def predecessor(self, node: Node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def successor(self, node: Node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def find(self, val: int):
        def dfs(node: Node):
            if node is None:
                return None
            if val < node.val:
                return dfs(node.left)
            elif val > node.val:
                return dfs(node.right)
            return node
        return dfs(self.root)

    def pre_order(self):
        res = []
        def dfs(node: Node):
            if node is None:
                return
            res.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(self.root)
        return res

    def in_order(self):
        res = []
        def dfs(node: Node):
            if node is None:
                return
            dfs(node.left)
            res.append(node)
            dfs(node.right)
        dfs(self.root)
        return res

    def post_order(self):
        res = []
        def dfs(node: Node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node)
        dfs(self.root)
        return res
    
    def bfs(self):
        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node:
                continue
            print(node.val)
            q.append(node.left)
            q.append(node.right)


if __name__ == "__main__":
    bst = BSTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(7)
    bst.insert(8)
    bst.insert(6)
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    bst.insert(25)
    bst.insert(18)
    bst.insert(23)
    print(bst.pre_order())
    print(bst.in_order())
    print(bst.post_order())
    print(bst.find(23))
    bst.bfs()