class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # reverse the strings
        a = a[::-1]
        b = b[::-1]
        res = []
        # result array (remember we want a string)
        max_len = max(len(a), len(b))
        # we need to iterate over the max length of either number
        carry = 0  # carry variable
        for i in range(max_len):
            a_digit = int(a[i]) if i < len(a) else 0
            b_digit = int(b[i]) if i < len(b) else 0
            # get digit, if its past the range of the number we're looking at just make it 0
            print(a_digit, b_digit, carry)
            digit_sum = a_digit + b_digit + carry
            # get the digit sum + the carry
            carry = 0
            # reset the carry because we've used it
            final_sum = digit_sum % 2
            # get the final sum with mod, if its above 2 we can just mod it, the most it can be is 3 (1 + 1 + 1) 3 % 2 == 1
            res.append(str(final_sum))
            if digit_sum > 1:  # if the digit sum is above 1 that means that there was a carry
                carry = 1
        if carry:  # if theres a carry at the end add 1 to the result
            res.append("1")

        res = res[::-1]  # reverse the result before we use it
        return "".join(res)
