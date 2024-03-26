# 200. Number of Islands
# Medium
# Given an m x n 2D binary grid grid which represents
# a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# things we need
# set to track all of the visited locations

import collections
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    visited = set()
    islands = 0
    rows = len(grid)
    cols = len(grid[0])

    def bfs(row_cord, col_cord):
        q = collections.deque()  # make a queue to add locations to search from
        visited.add((row_cord, col_cord))  # visited the start location
        q.append((row_cord, col_cord))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, up, down
        while q:
            row, col = q.popleft()  # need to look up why changing the popleft to a pop would make this a DFS
            for dr, dc in directions:
                d_row = row + dr
                d_col = col + dc

                if (d_row in range(rows) and
                        d_col in range(cols) and
                        grid[d_row][d_col] == "1" and
                        (d_row, d_col) not in visited):
                    q.append((d_row, d_col))
                    visited.add((d_row, d_col))
                    # if we've never visited that land before and its in bounds add it to the queue to search from

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited and grid[r][c] == "1":
                bfs(r, c)  # point of BFS is to mark all the land from a single point as visited
                islands += 1
    return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(num_islands(grid))
