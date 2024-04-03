# 424. Longest Repeating Character Replacement
# Medium

# You are given a string s and an integer k. You can choose any character of the string
# and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the
# same letter you can get after performing the above operations.
#
#
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AAABABB", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

# need to find condition in which the length of the current window - max freq of char = k

# ex: BABB
# length of window = 4
# k = 1 for this example
# 4 - (3) = 1 k

def character_replacement(s: str, k: int) -> int:
    window_map = {}
    l = 0
    res = 0
    for r in range(len(s)):
        window_map[s[r]] = 1 + window_map.get(s[r], 0)

        # get length of current window minus the max char count in the window
        # IE if k == 1 and we have "AABA" max(count.values()) should return 3
        # and the length of the current window is 4 so which is within target of what we're trying to
        # find
        # if its greater than then we want to move the left pointer as thats too many chars
        if (r - l + 1) - max(window_map.values()) > k:
            window_map[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


print(character_replacement("AABABBA", 1))
