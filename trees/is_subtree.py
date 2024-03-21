# 572. Subtree of Another Tree
# Easy

# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree
# and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
#
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104
# Initial thoughts:
# need to find the matching parent node first, then check if its the same tree

# dont actually need to find matching parent node, just recursivly check left and right down the tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    if subRoot and not root:
        return False

    if is_same_tree(root, subRoot):
        return True

    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if (p and q) and (p.val == q.val):
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    return False
