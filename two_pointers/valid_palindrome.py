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


# if we dont use the builtin functions we can determine if its a character by checking if character is alphanumeric
# by checking ord values
# ie: ord('A') <= ord('Z') etc for a,z and 0,9.  all of those characters are in order for their ord value


def is_char_or_num(s: str) -> bool:
    print(f"checking if {s} is a char or num")
    ord_in = ord(s)
    print(ord_in)
    return (
        ord("A") <= ord_in <= ord("Z")
        or ord("a") <= ord_in <= ord("z")
        or ord("0") <= ord_in <= ord("9")
    )


def is_palendrome_no_memory(s: str) -> bool:
    if len(s) <= 1:
        return True
    p = 0
    q = len(s) - 1
    while p < q:
        # need p < q conditional so we dont go out of bounds
        while p < q and not is_char_or_num(s[p]):
            p += 1
        while p < q and not is_char_or_num(s[q]):
            q -= 1
        # once both are alphanumeric we can do == comparision
        if s[p].lower() != s[q].lower():
            return False
        p += 1
        q -= 1
    return True


print(is_palendrome_no_memory("A man, a plan, a canal: Panama"))
