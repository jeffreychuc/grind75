# 56. Merge Intervals
# Solved
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
# Constraints:
#
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        # Output: [[1,6],[8,10],[15,18]]
        res = []
        # base case
        if not intervals:
            return res

        # NB: if you dont sort the intervals this comparison wont work
        # intervals.sort(key=lambda k: k[0])
        intervals.sort()  # the sort function will use the first element in the list to sort
        curr = intervals[0]
        # set curr to start of intervals
        # iterate starting from ele 1
        for inter in intervals[1:]:
            # if start of the interval in the list is >= the start of the current and less than or == to the end
            # merge
            if inter[0] <= curr[1]:
                new_start = min(curr[0], inter[0])
                new_end = max(curr[1], inter[1])

                curr = [new_start, new_end]
            else:
                # else append the current and set the interval we're looking at to the new current
                res.append(curr)
                curr = inter
        # final append
        res.append(curr)
        return res
