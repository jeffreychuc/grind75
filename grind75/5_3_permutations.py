# 46. Permutations
# Solved
# Medium
# Topics
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        if len(nums) == 1:
            return [nums[:]]  # we want to make a copy of this list so it doesnt pass by reference

        for _ in range(len(nums)):
            n = nums.pop(0)  # removes first element from list
            perms = self.permute(nums)  # recusively call permute to get all purmutations of sublist

            # for each sub permutation that was returned, add the inital digit
            # that was popped off
            for perm in perms:
                perm.append(n)
            # extend the result list with perms
            results.extend(perms)
            nums.append(n)

        return results
