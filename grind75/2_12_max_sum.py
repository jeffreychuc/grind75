from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # i think you can take two pointers one left and right and
        # possibly if its a negative number shift the pointer in
        #  and just keep a MAX

        # l, r = 0, len(nums)
        # max_sum = nums[0]
        # while l < r:
        #     # [l:r] is not inclusive on the r
        #     curr_sum = sum(nums[l:r])
        #     print(f"sum of {nums[l:r]} is {sum(nums[l:r])}")
        #     print(f"l is {l}, r is {r}")
        #     max_sum = max(max_sum, curr_sum)
        #     # need to minus 1 for the r because r is + 1 to make the array slicing work
        #     if nums[l] < nums[r - 1]:
        #         l += 1
        #     else:
        #         r -= 1

        # return max_sum

        # dont need two pointers, idea is that youre looking for the max subarray, so we can start from the
        # left and just keep adding until we go negative then we can reset to 0

        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)

        return max_sum
