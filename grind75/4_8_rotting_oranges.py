import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count all fresh oranges?
        queue = collections.deque()
        time = 0
        fresh = 0

        ROW = len(grid)
        COL = len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue and fresh > 0:
            for i in range(len(queue)):
                # pop left because we want to pull from the oldest cords not the new ones we just added
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # make sure that coords are in bounds and fresh
                    if row < 0 or row == ROW or col < 0 or col == COL or grid[row][col] != 1:
                        continue
                    # make orange rotten
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
