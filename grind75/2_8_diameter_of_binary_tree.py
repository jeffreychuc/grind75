from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameter_of_binaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs down, take max of left or right tree
        # at root add left + right?

        # dfs should return height of tree, but diameter is the height of the left and right
        # so you keep a global variable outside of the dfs to keep track of the MAX diameter
        # that you've ever seen
        # included PNG has an example of a tree that has a diameter that is max not from the root
        res = 0

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            # diameter is the longest path from two nodes within a tree
            diameter = 2 + left + right
            nonlocal res  # we can either nonlocal res here or we can make res an array and index into it
            res = max(res, diameter)
            return 1 + max(left, right)

        dfs(root)

        return res
