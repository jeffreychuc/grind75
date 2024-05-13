class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two types of palindromes, even and odd ones
        # even = bb
        # odd = bab
        # we can start a middle out search from each index of chars in the string
        # on starting from the char and one starting from i, i+1
        res = ""
        for i in range(len(s)):
            max_len_odd_str = self.search_from_index(s, i, i)
            max_len_even_str = self.search_from_index(s, i, i + 1)
            local_res = ""
            if len(max_len_odd_str) > len(max_len_even_str):
                local_res = max_len_odd_str
            else:
                local_res = max_len_even_str

            if len(res) < len(local_res):
                res = local_res
        return res

    # babad
    # 01234
    def search_from_index(self, s: str, s_1: int, s_2: int):
        # s_1 will go left, s_2 will go right
        res = ""
        while s_1 >= 0 and s_2 < len(s) and s[s_1] == s[s_2]:
            res = s[s_1:s_2 + 1]
            s_1 -= 1
            s_2 += 1

        return res
