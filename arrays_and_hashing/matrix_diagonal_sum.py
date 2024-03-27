# 1572. Matrix Diagonal Sum
# Easy

# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and
# all the elements on the secondary diagonal that are not part of the primary diagonal.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# Example 2:
#
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:
#
# Input: mat = [[5]]
# Output: 5
#
#
# Constraints:
#
# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100

from typing import List


def diagonal_sum(mat: List[List[int]]) -> int:
    res = 0
    row = len(mat)
    col = len(mat[0])
    # we can do this assuming the cols are consistent
    cords = set()  # using a set to dedupe existing cords

    x, y = 0, 0
    while x < row and y < col:
        cords.add((x, y))
        x += 1
        y += 1

    x, y = row - 1, 0
    while x >= 0 and y < col:
        cords.add((x, y))
        x -= 1
        y += 1

    for x, y in cords:
        res += mat[x][y]

    return res


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(diagonal_sum(mat))
