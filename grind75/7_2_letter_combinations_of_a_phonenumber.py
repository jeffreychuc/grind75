# 17. Letter Combinations of a Phone Number
# Solved
# Medium
# Topics
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        self.letter_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # follow backtracking pattern
        # call backtrack function with index and accumulator

        self.res = []

        if not digits:
            return self.res

        self.backtrack(digits, 0, [])

        return self.res

    def backtrack(self, digits: str, curr_idx: int, curr_res: List[str]):
        # if we've collected enough letters
        if curr_idx == len(digits):
            res = "".join(curr_res)
            self.res.append(res)
            return

        for c in self.letter_mapping[digits[curr_idx]]:
            curr_res.append(c)
            self.backtrack(digits, curr_idx + 1, curr_res)
            # this removes the search for the initial, so we can move on to the next
            # IE: so if we did a + all its combos, we now remove A and add B in and do B + all its combos
            # this pop would remove the letter A, so we move on to B
            curr_res.pop()
