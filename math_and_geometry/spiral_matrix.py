# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    top, left = 0, 0
    bottom = len(matrix)
    right = len(matrix[0])
    res = []
    while left < right and top < bottom:
        # get the top row first
        for p in range(left, right):
            # print(f"[{top}, {p}]")
            res.append(matrix[top][p])
        # move top pointer from top row down one
        top += 1

        # go from top row to bottom row
        for p in range(top, bottom):
            # print(f"[{p}, {right - 1}]")
            res.append(matrix[p][right - 1])
        # move right pointer left one
        right -= 1

        # go from right to left in reverse for the bottom row
        for p in range(right - 1, left - 1, -1):
            # print(f"[{bottom - 1}, {p}]")
            res.append(matrix[bottom - 1][p])
        # move bottom pointer up 1
        bottom -= 1

        # go from bottom to top for the left most column
        for p in range(bottom - 1, top - 1, -1):
            # print(f"[{p}, {left}]")
            res.append(matrix[p][left])
        left += 1
    return res


print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
