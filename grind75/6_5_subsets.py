# 78. Subsets
# Medium
# Topics
# Companies
# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        self.res = []

        # base case, if there's no numbers in nums just return an empty array
        if not nums:
            return self.res

        # call backtracking at index 0
        self.backtrack(nums, 0, [])

        # return res
        return self.res

    def backtrack(self, nums: List[int], curr_idx: int, curr_res: List[int]):
        # base case, if the current index == the length of nums, append a copy to the result
        if curr_idx == len(nums):
            self.res.append(curr_res[:])
            return

        # do not include the current number in the solution set
        self.backtrack(nums, curr_idx + 1, curr_res)
        # going down this path all the way to the left means that we never include any of the
        # numbers at the curr_idx in the nums array so when we get to curr_idx == len(nums) it will return an
        # empty array

        # include current number in solution
        curr_res.append(nums[curr_idx])
        self.backtrack(nums, curr_idx + 1, curr_res)
        curr_res.pop()
