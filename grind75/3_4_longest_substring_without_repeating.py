# 3. Longest Substring Without Repeating Characters
# Solved
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

# solution is to use two pointers, one left one right.

# as you move through the string, add each character from the right pointer into a set
# could probably do this with a hashmap with some more logic if you dont have access to a set class
# as we're moving through, if we see that the character on the right is in the substring, move the
# left pointer to the right one step at a time until all the characters are unique again.
# the length of the substring is (r - 1 + 1) the +1 is from the fact that the pointers are 0 indexed


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        max_substring_len = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            current_substring_len = r - l + 1
            max_substring_len = max(max_substring_len, current_substring_len)

        return max_substring_len
