from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # this is the stack we're going to keep of all the elements we're queueing to go through

        while True:  # dont break unless return, this is ok because the value is guarenteed
            while root:  # if there is a node, add it to the stack and go left
                stack.append(root)
                root = root.left

            root = stack.pop()  # pop the last node off the stack
            k -= 1  # sub one from k

            if k == 0:  # if we've reached k == 0 that means its the element we want
                return root.val

            root = root.right  # try to traverse right on the node we're currently on
