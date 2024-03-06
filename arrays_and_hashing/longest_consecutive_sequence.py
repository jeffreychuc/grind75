# 128. Longest Consecutive Sequence
# Medium
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Inital thoughts would be to sort the array
# but that would be nlogn

# Notes, we can get the start of each sequence by checking if each value has a left neighbor.
# in the above array, 1 has no left neighbor, 100 has no left neighbor, 200 has no left neighbor
# when we have each left neighbor we can check to see if the next value is in the array

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    curr_max_seq = 0
    num_set = set(nums)
    # using a set speeds up lookup because we will remove duplicates
    for val in num_set:
        # check if prev value is there
        if (val - 1) not in num_set:
            # is start
            still_sequence = True
            next_val = val + 1
            sequence_length = 1
            while still_sequence:
                if next_val not in num_set:
                    still_sequence = False
                else:
                    sequence_length += 1
                    next_val += 1
            if curr_max_seq < sequence_length:
                curr_max_seq = sequence_length

    return curr_max_seq


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
