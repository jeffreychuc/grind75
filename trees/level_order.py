# Given the root of a binary tree, return the level order traversal
# of its nodes' values. (i.e., from left to right, level by level).
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
#
#
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    res = []  # result return array

    queue = collections.deque()  # init a new queue so we can popleft from it
    queue.append(root)  # add the root node to the queue

    while queue:  # while the queue exist
        level_res = []  # result for the current level
        for i in range(len(queue)):  # for each element in the queue right now loop
            curr_node = queue.popleft()  # pull node out of the queue
            if curr_node:
                level_res.append(curr_node.val)
                # add the value of the current node into the result array for the
                # current level of the tree we're looking at
                queue.append(curr_node.left)
                queue.append(curr_node.right)
                # add the left and right nodes to the end of the queue
        if level_res:
            res.append(level_res)
    return res
