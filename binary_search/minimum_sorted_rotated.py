# 153. Find Minimum in Rotated Sorted Array
# Medium

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
#
# Example 1:
#
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# First thoughts:
# would be easy if it was sorted, but this is a rotate array
# could search for "pivot" in the array where the values arnt increasing anymore
# solution uses binary search using a left and right pointer

# we pull a mid pointer and check if that value is >= the value at the left pointer
# if it is greater then the left values are all less than the mid pointer and we want to search right
# if not search left

from typing import List


def find_min(nums: List[int]) -> int:
    res = nums[0]  # init result with left value

    l = 0
    r = len(nums) - 1

    while l <= r:
        # i don't really get this conditional fully
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = (l + r) // 2  # floor division so rounds down to nearest whole number
        res = min(res, nums[m])
        # if the mid point is >= to the left portion, its in the "left sorted portion"
        if nums[m] >= nums[l]:
            # search right
            l = m + 1
        # else its in the "right sorted portion" and we should search left
        else:
            r = m - 1

    return res


print(find_min([4, 5, 6, 7, 0, 1, 2]))
print(find_min([0, 1, 2, 4, 5, 6, 7]))
print(find_min([3, 4, 5, 1, 2]))
print(find_min([11, 13, 15, 17]))
print(find_min([2, 1]))
