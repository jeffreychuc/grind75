"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned_nodes = {}  # key is the value of the cloned node, value would be the node

        def dfs(n: Optional['Node']):
            if not n:
                return n

            if n.val in cloned_nodes:
                return cloned_nodes[n.val]

            cloned_node = Node(n.val)  # make a copy of the node
            cloned_nodes[n.val] = cloned_node  # place pointer into hashmap for cloned node

            for nei in n.neighbors:
                cloned_node.neighbors.append(dfs(nei))  # add each neighbor into the cloned_node neighbors

            return cloned_node

        return dfs(node)
