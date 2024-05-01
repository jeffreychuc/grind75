import collections

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW = len(mat)
        COL = len(mat[0])

        # first thing is to fill a queue with all 0's we want to start searching from all the 0's on the matrix
        queue = collections.deque()

        for r in range(ROW):
            for c in range(COL):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = '#'

        # queue should now be filled with all of the 0's on the mat
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            r, c = queue.popleft()
            # search all 4 directions from origin of z_loc
            for dr, dc in dirs:
                if 0 <= (r + dr) < ROW and 0 <= (c + dc) < COL and mat[r + dr][c + dc] == '#':
                    # take origin value + 1 and set that == to the cell that has the # sign
                    mat[r + dr][c + dc] = mat[r][c] + 1
                    # add to queue the cell we just mutated
                    queue.append((r + dr, c + dc))

        return mat
