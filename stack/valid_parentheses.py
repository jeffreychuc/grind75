# 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def is_valid(s: str) -> bool:
    open_paren_map = {"{": "}", "(": ")", "[": "]"}
    open_paren = list(open_paren_map.keys())
    close_paren = list(open_paren_map.values())
    close_paren_arr = []
    for c in s:
        if c in open_paren:
            close_paren_arr.append(open_paren_map[c])
        if c in close_paren:
            if len(close_paren_arr) == 0:
                return False
            res = close_paren_arr.pop()
            if c != res:
                return False
    if len(close_paren_arr) != 0:
        return False
    return True


print(is_valid("[]"))
print(is_valid("]["))
print(is_valid("(["))
print(is_valid("([])"))
print(is_valid("([]]"))
