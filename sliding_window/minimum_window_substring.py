# 76. Minimum Window Substring
# Hard
# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
#
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
# Constraints:
#
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?


# print(min_window("ADOBECODEBANC", "ABC"))

# {A: 1, B: 1, C:1}


def min_window(source: str, target: str) -> str:
    target_map = {}  # map with the target chars as keys + counts
    window_map = {}  # map with the current sliding windows chars + counts
    res_r, res_l = 0, 0  # right and left coord of the last good known substring
    res_length = float("infinity")  # length of the last good known substring
    # make map for target comparison
    for c in target:
        target_map[c] = 1 + target_map.get(c, 0)

    # init left pointer
    l = 0
    # count of the number of characters in the target_map that we've currently found
    found_chars = 0
    # count of the number of characters taht we need
    need_chars = len(target_map)

    # for loop over the string char by char
    for r, c in enumerate(source):
        # add each char to the window map
        window_map[c] = 1 + window_map.get(c, 0)
        # if the character we just added is in the target map and the counts required
        # in the target map are met for that char, add one to the found_chars variable
        if c in target_map and window_map[c] == target_map[c]:
            found_chars += 1
        # if the number of found chars is == number of need chars
        while found_chars == need_chars:
            # update l,r cords for res
            # update res_length
            if (r - l + 1) < res_length:
                res_length = r - 1 + 1
                res_r = r
                res_l = l
            window_map[source[l]] -= 1
            l += 1
            if source[l] in target_map and window_map[source[l]] < target_map[source[l]]:
                found_chars -= 1
    return source[res_l:res_r + 1]


print(min_window("ADOBECODEBANC", "ABC"))
print(min_window("a", "a"))
