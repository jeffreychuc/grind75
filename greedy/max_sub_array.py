# 53. Maximum Subarray
# Medium
# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
#
# Follow up: If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List


def max_sub_array(nums: List[int]) -> int:
    max_sub = nums[0]
    curr = 0
    max_element = nums[0]
    # this is a modification of Kadane’s algorithm.
    # Kadane’s algo only works if there's at least
    # one positive element
    for n in nums:
        # we keep track of the "max_element" so we can return that if the max_sub is < 0
        max_element = max(max_element, n)
        if n < 0:
            curr = 0
        curr += n
        max_sub = max(curr, max_sub)

    return max_sub if max_sub > 0 else max_element


print(max_sub_array([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
