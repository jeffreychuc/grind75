# 100. Same Tree
# Easy
#
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
#
# Initial Thoughts:
# equality is based on structure and on value stored in node, so check value and make sure
# both of them arnt None

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if (p and q) and (p.val == q.val):
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    return False
