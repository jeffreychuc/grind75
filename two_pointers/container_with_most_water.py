# 11. Container With Most Water
# Medium

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
#
#
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# Initial thoughts:
# brute force way would be to do 2 sum ii but instead of the sum you find the max area

from typing import List


# def max_area(height: List[int]) -> int:
#     # brute force solution
#     res = 0
#     for x, y in enumerate(height):
#         second_pointer = x + 1
#         while second_pointer <= len(height) - 1:
#             width = second_pointer - x
#             h = min(y, height[second_pointer])
#             total_volume = width * h
#             if total_volume > res:
#                 res = total_volume
#             second_pointer += 1
#
#     return res
def max_area(height: List[int]) -> int:
    # two pointer solution
    res = 0
    left_pointer = 0
    right_pointer = len(height) - 1
    while left_pointer < right_pointer:
        curr_area = min(height[left_pointer], height[right_pointer]) * (
            right_pointer - left_pointer
        )
        if curr_area > res:
            res = curr_area
        if height[left_pointer] > height[right_pointer]:
            right_pointer -= 1
        else:
            left_pointer += 1

    return res


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
