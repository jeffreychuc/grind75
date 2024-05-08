# 79. Word Search
# Solved
# Medium
# Topics
# Companies
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once.
#
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
# Constraints:
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS solution

        # base case
        if not word:
            return True

        # go through board and search for start character
        # search from those start points,

        # setting our constants
        self.ROW = len(board)
        self.COL = len(board[0])

        # visited set is so we dont backtrack into a cell we've already seen to create a word
        visited = set()
        start_char = word[0]
        # going through the whole board to find the start character to init a DFS search from that point
        for r in range(self.ROW):
            for c in range(self.COL):
                if board[r][c] == start_char:
                    # we want to pass in the board, start cord for search, and a visited set to keep track of cells
                    # we've seen if it returns true we want to return true for the whole thing
                    if self.dfs(board, (r, c), word, visited):
                        return True
        # if nothing can return true we return false because we cant find a sutable path
        return False

    def dfs(self, board: List[List[str]], cord: tuple[int, int], word: str, visited: set[tuple[int, int]]) -> bool:
        # base case, if there's an empty "word" passed in that means the entire word has been found we can return true
        if not word:
            return True
        # somehow we need a visited set here

        r, c = cord
        # make sure cord is not in visited and make sure the character we're looking for is true
        if (r, c) not in visited and r >= 0 and r < self.ROW and c >= 0 and c < self.COL and board[r][c] == word[0]:
            visited.add((r, c))
            # add to visited, then search all 4 directions from that point
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dirs:
                if self.dfs(board, (r + dr, c + dc), word[1:], visited):
                    return True
            # if none of the directions return true remove the visted cord
            visited.remove((r, c))
        return False
