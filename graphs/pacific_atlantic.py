# 417. Pacific Atlantic Water Flow
# Medium

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
# The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells.
# You are given an m x n integer matrix heights where heights[r][c] represents
# the height above sea level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly
# north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
# Water can flow from any cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that
# rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
#
#
#
# Example 1:
#
#
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:
#
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
#
#
# Constraints:
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

# DFS from cells touching pacific (top right) and get one set of answers
# DFS from cells touching atlantic (bottom right)
# find intersection of solutions

from typing import List, Set


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    pacific = set()
    atlantic = set()
    row = len(heights)
    col = len(heights[0])

    def dfs(x: int, y: int, ocean: Set, prev_height: int):
        # if we've already visited a location
        # or if x is out of bounds or if y is out of bounds
        # or ir x is hitting the edge or if y is hitting the edge
        # or if the height is less than the prev_height
        if (x, y) in ocean or x < 0 or y < 0 or x == row or y == col or heights[x][y] < prev_height:
            return
        ocean.add((x, y))
        # now check all 4 neighbors
        dfs(x + 1, y, ocean, heights[x][y])
        dfs(x - 1, y, ocean, heights[x][y])
        dfs(x, y + 1, ocean, heights[x][y])
        dfs(x, y - 1, ocean, heights[x][y])

    # check the top and bottom row of the matrix, pacific touching and atlantic touching
    for y in range(col):
        dfs(0, y, pacific, heights[0][y])
        dfs(row - 1, y, atlantic, heights[row - 1][y])

    # check the left and right col of the matrix, pacific touching and atlantic touching
    for x in range(row):
        dfs(x, 0, pacific, heights[x][0])
        dfs(x, col - 1, atlantic, heights[x][col - 1])

    res = pacific.intersection(atlantic)
    return [[x, y] for x, y in res]


h = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]

print(pacific_atlantic(h))
