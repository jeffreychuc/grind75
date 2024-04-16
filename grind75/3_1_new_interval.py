# 57. Insert Interval
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105from
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals are non overlapping
        # intervals are sorted
        # dont need to modify in place

        res = []
        for i, inter in enumerate(intervals):
            # if the end of the incoming interval is
            # less than the start of the newInterval
            # then append to res and skip
            # print(f"newInterval {newInterval}, inter {inter}")
            if inter[1] < newInterval[0]:
                res.append(inter)
            # if the start of the incoming interval is > than the end of the newInterval, time to append and return everything
            elif inter[0] > newInterval[1]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                newInterval[0] = min(inter[0], newInterval[0])
                newInterval[1] = max(inter[1], newInterval[1])
        # base case of no end, append newInterval and return
        res.append(newInterval)
        return res
