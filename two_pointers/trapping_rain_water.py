# 42. Trapping Rain Water
# Solved
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


from typing import List


def trap(height: List[int]) -> int:
    # volume is === min - height, only add if positive
    # min_volume_for_section = min(height[start], height[end])
    max_left = [0] * len(height)  # looking for the max height to the left of the current indexed position
    max_right = [0] * len(height)  # looking for the max height to the right of the current indexed position

    res = 0
    for i in range(1, len(height)):
        max_left[i] = max(height[i - 1], max_left[i - 1])
    for i in range(len(height) - 2, -1, -1):
        print(i)
        max_right[i] = max(height[i + 1], max_right[i + 1])

    for i in range(len(height)):
        min_volume = min(max_left[i], max_right[i])
        res += max(min_volume - height[i], 0)

    return res
