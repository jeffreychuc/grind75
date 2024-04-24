# 200. Number of Islands
# Solved
# Medium
# Topics
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
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

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        visited = set()
        island_count = 0

        def dfs(r: int, c: int):
            if (r, c) in visited or r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == '0':
                return

            visited.add((r, c))
            # dfs up down left right
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    island_count += 1

        return island_count
