# Given an integer array nums, return true if any value appears at least twice in the array, and return false if
# every element is distinct.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# first thoughts would be to use a hashmap to track seen values

from typing import List


# Time: O(n)
# Space: O(n)
def contains_duplicate(nums: List[int]) -> bool:
    vals_map = {}
    for val in nums:
        if val in vals_map:
            return True
        vals_map[val] = True
    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
