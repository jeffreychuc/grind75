# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
#

from typing import Dict


# Time: O(N)
# Space: O(N)
def is_anagram(s: str, t: str) -> bool:
    # if the lengths aren't === fail fast
    if len(s) != len(t):
        return False
    # there is a python datastructure called Counter() that takes in
    # a string and returns a hashmap with the count
    # from collections import Counter

    input_char_count = get_char_count(s)
    for c in t:
        if c in input_char_count:
            input_char_count[c] -= 1
            if input_char_count[c] == 0:
                del input_char_count[c]
        else:
            return False
    # you can run bool(dict) to check if a dict has any keys in it
    if bool(input_char_count):
        return False
    return True


def get_char_count(s: str) -> Dict:
    res = {}
    for c in s:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


def is_anagram_no_extra_space(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram_no_extra_space("anagram", "nagaram"))
print(is_anagram_no_extra_space("rat", "car"))
