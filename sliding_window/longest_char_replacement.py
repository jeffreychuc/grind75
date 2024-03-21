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
    l = 0
    res = 0
    count = {}

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        print(count)
        # length_of_window = r - l + 1
        if (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1  # remove count of character from left character
            l += 1  # shift left pointer right

        res = max(res, r - l + 1)
        print(res)

    return res


print(character_replacement("AABABBA", 1))
