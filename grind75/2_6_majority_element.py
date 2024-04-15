# 169. Majority Element
# Solved
# Easy
# Topics
# Companies
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?


from typing import List


# uses Boyer Moore Majority Vote Algorithm
# to keep space O(1)
# time is linear O(2n) == O(n)
# https://www.youtube.com/watch?v=gY-I8uQrCkk

def majority_element(nums: List[int]) -> int:
    n = len(nums)

    candidate = -1
    count = 0
    for ele in nums:
        if ele == candidate:
            count += 1
        elif count == 0:
            candidate = ele
            count = 1
        else:
            count -= 1

    # for this specific problem we don't need the
    # verification step because
    # the problem guarantees that there is a majority candidate
    # if it didnt exist we would need to verify that the candidate
    # actually had a majority count
    # ie: input would be [2,1,2,2,2,1,1,3]  2 has 4 occurrences but
    # there's 8 total elements so it's not a majority
    count = 0
    for ele in nums:
        if ele == candidate:
            count += 1

    return candidate if count > n / 2 else -1
