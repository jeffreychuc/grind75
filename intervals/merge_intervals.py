# 56. Merge Intervals
# Medium
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
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


def merge(intervals: List[List[int]]) -> List[List[int]]:
    res = []

    intervals.sort(key=lambda k: k[0])
    new_interval = intervals[0]
    for i, inter in enumerate(intervals[1:]):

        start, end = inter
        start_new_inter, end_new_inter = new_interval

        if end_new_inter < start:
            res.append(new_interval)
            new_interval = inter
        elif start_new_inter > end:
            res.append(inter)
        else:
            new_interval = [min(start, start_new_inter), max(end, end_new_inter)]
            print(f"new interval is ${new_interval}")
    if new_interval:
        res.append(new_interval)
    return res


# print(merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
print(merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]))


# neetcode solution
def merge_neetcode(intervals: List[List[int]]) -> List[List[int]]:
    res = [intervals[0]]
    intervals.sort(key=lambda k: k[0])
    for start, end in intervals[1:]:
        last_end = res[-1][1]  # get last element and get end
        if start <= last_end:
            res[-1][1] = max(last_end, end)
        else:
            res.append([start, end])

    return res


print(merge_neetcode([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]))
