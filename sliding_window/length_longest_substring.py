# 3. Longest Substring Without Repeating Characters
# Attempted
# Medium
# Topics
# Companies
# Given a string s, find the length of the longest
# substring
#  without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


def length_of_longest_substring(s: str) -> int:
    res = 0
    p = 0
    q = 1
    while q <= len(s):
        curr_sub = s[p:q]
        curr_sub_set = set(curr_sub)
        if len(curr_sub) != len(curr_sub_set):
            # there's a repeat, move left pointer
            p += 1
        else:
            res = max(res, len(curr_sub))
            q += 1
    return res


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring(" "))
