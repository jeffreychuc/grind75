import collections


class Solution:
    def myAtoi(self, s: str) -> int:
        # 1 read in and ignore any white space
        s = s.lstrip()
        # we keep a boolean to determine if we need to make the result negative or not
        negative = False

        # base case, if theres no string return 0
        if not s:
            return 0

        # if the string starts with -
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            # if the string starts with + we should remove it from parsing
            s = s[1:]

        res = ""
        for c in s:
            # if the ord of the char is between 48 and 57 then its a number
            # we could also replace this with
            # if c.isdigit()
            if 48 <= ord(c) <= 57:
                res = res + c
            else:
                break
        # making the max and min int clamping constants
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -1 * (2 ** 31)

        # if theres no digits added to the res string just return 0
        if not res:
            return 0

        # convert res to an int
        res = int(res)
        # if the result is supposed to be negative, return the "max" of either the min_int constant
        # or the result * -1.  the "max" will be whatever number is larger than the clamping value
        if negative:
            return max(MIN_INT, res * -1)

        # if the result should be positive, should be the min of either the max int or if the result is below that
        return min(MAX_INT, res)
