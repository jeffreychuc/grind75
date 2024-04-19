# 102. Binary Tree Level Order Traversal
# Solved
# Medium
# Topics
# Companies
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is a binary search...
        # need a queue, add left and right to the queue and then in order keep adding to the queue after you finish
        # each level
        res = []
        if not root:
            return res
        queue = collections.deque()
        # add root to the queue
        queue.append(root)

        while queue:
            num_nodes = len(queue)
            # we want this to be a fixed number as we only want to
            # process the nodes that are in that level
            level = []  # each level is going to be returned in its own list
            for _ in range(num_nodes):  # only pop the number of nodes in the level we're at
                node = queue.popleft()
                if node:  # nodes can be null if the left wasnt pointing to anything
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            if level:  # only append the level if there was something in the list
                res.append(level)
        return res
