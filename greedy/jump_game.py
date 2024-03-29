# https://www.youtube.com/watch?v=Zb4eRjuPHbM

# 55. Jump Game
# Medium
# Topics
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

from typing import List


def can_jump(nums: List[int]) -> bool:
    last_good_index = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        # check if from the current position in the array we're looking at we can get to
        # the last good index.
        # ie: want to get to index 4, at position 3 we can go + 2.
        # so position + val_at_position >= goal/last_good_index
        if i + nums[i] >= last_good_index:
            last_good_index = i

    return True if last_good_index == 0 else False


print(can_jump([2, 3, 1, 1, 4]))
print(can_jump([3, 2, 1, 0, 4]))
