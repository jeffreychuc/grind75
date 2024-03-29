# 98. Validate Binary Search Tree
# Medium
# Topics
# Companies
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def is_valid(node: Optional[TreeNode], left_boundry: int, right_boundry: int) -> bool:
        if not node:
            return True

        if node.val < left_boundry or node.val > right_boundry:
            return False

        return is_valid(node.left, left_boundry, node.val) and is_valid(node.right, node.val, right_boundry)

    return is_valid(root, float("-inf"), float("inf"))
