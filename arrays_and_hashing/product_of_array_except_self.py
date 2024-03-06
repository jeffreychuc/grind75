# 238. Product of Array Except Self
# Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra
# space for space complexity analysis.)

# Initial thoughts:
# no division... seems like you can just iterate through the original array using the index and get the values
# of the other indexes?

from typing import List


# def product_except_index(nums: List[int], index: int) -> int:
#     res = 1
#     for i, val in enumerate(nums):
#         if i != index:
#             res *= val
#     return res
#
#
# def product_except_self(nums: List[int]) -> List[int]:
#     res = []
#     for i, _ in enumerate(nums):
#         res.append(product_except_index(nums, i))
#     return res


# NB: above solution is too slow...

# every value in the array is the product of the values before and after the value in the array
# ie: [1,2,3,4]
#     position 0 is
#     1 * (2*3*4)

#     position 1 is
#     1 * (3*4)

#     position 2 is
#     (1*2) * 4

# knowing this we can pre-calculate the left value for the product and then multiply that by the right value
# of the product


def product_except_self(nums: List[int]) -> List[int]:
    res = [1] * (len(nums))  # makes an array of all 1's the length of nums

    prefix = 1
    for i in range(len(nums)):
        # place prefix in current result location
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        # multiply the postfix by what's stored in the prefix
        res[i] *= postfix
        # update the postfix value by multiplying by what's in the nums
        postfix *= nums[i]

    return res
