# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Initial thoughts:
# we want to have a hashmap of the values of each of the values first,
# then we need to pick out the top k values out of that
# and return that list
# we can use a bucket sort to keep things in order


from typing import List

# Time: O(N)
# Space: O(N)


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # this bucket could also be a list instead of a hashmap...
    # bucket = [[] for i in range(len(nums) + 1)]
    bucket = {}
    # init buckets to drop values into them
    for i in range(1, len(nums) + 1):
        bucket[i] = []

    # enumerate counts
    counter = {}
    for i in nums:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    # for each key in the counter drop it into the buckets
    for key in counter.keys():
        bucket[counter[key]].append(key)

    res = []
    # could so do range(len(nums) + 1, 0, -1) instead of reversing it
    for i in reversed(range(1, len(nums) + 1)):
        curr_bucket = bucket[i]
        for element in curr_bucket:
            res.append(element)
            if len(res) == k:
                return res
    return res


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
