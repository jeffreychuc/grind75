# 125. Valid Palindrome
# Easy
#
# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
# characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
#
# Constraints:
#
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Initial thoughts: use two pointers at the start and end of the string sequence to check each character
# we need to remove non characters from the string though...
# NB: we want to keep alpha and numeric characters

# python has a .isascii() function so we can probably chain that with .lower to get a sanitized string
# .isascii isn't correct, we want isalpha


def is_palindrome(s: str) -> bool:
    sanitized_string_arr = [
        char.lower() for char in s if char.isalpha() or char.isalnum()
    ]
    if len(sanitized_string_arr) <= 1:
        return True
    p = 0
    q = len(sanitized_string_arr) - 1
    while p <= q:
        # print(
        #     f"checking {sanitized_string_arr[p]} {p} == {sanitized_string_arr[q]} {q}"
        # )
        if sanitized_string_arr[p] != sanitized_string_arr[q]:
            return False
        p += 1
        q -= 1
    return True


print(is_palindrome("Aa"))
print(is_palindrome("A man, a plan, a canal: Panama"))
