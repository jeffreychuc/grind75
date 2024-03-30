# 33. Search in Rotated Sorted Array
# Medium
# Topics
# Companies
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot
# index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ...,
# nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

# Initial thoughts:
# should be a binary search, use 3 pointers L,M,R
# if value of L > what you're searching for go right of the mid

from typing import List


def search(nums: List[int], target: int) -> int:
    res = -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        # we recalculate the mid everytime because we want to shift the window
        # in which we're looking at
        if nums[mid] == target:
            return mid

        # if the left pointer is <= the number in the middle we know were looking at the "left sorted portion"
        # IE: [4,5,6,7,0,1,2]
        # mid == pos 3 or value 7
        # left == 4
        # left <= mid is true 4 <= 7
        if nums[left] <= nums[mid]:
            # if the target is greater than the mid or the target is less than the left value, we want to search right
            # [4,5,6,7,0,1,2]
            # target == 0
            # target is < than the mid (7) and the target is < 4.  so we want to search right
            if target > nums[mid] or target < nums[left]:
                # search right
                # left is now == to pos 4 value 0
                left = mid + 1
            else:
                # else search left, we set the right most pointer to the left value of mid
                right = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return res


# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([1000, 1001, 1, 4, 6, 999], 999))
