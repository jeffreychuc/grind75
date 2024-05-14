import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # keep a map of the chars in p
        # have a l and r pointer,
        res = []

        # base case, if p is > than s in length it will never work
        if len(p) > len(s):
            return res

        # init a p_map which is just a map of all the chars in the p string
        p_map = collections.defaultdict(int)
        for c in p:
            p_map[c] += 1

        # init l and r pointers
        l = 0
        r = len(p) - 1

        s_map = collections.defaultdict(int)
        # init s_map?
        for i in range(len(p)):
            s_map[s[i]] += 1

        while r < len(s):
            # we can do map equality in python
            if s_map == p_map:
                res.append(l)

            # del l index char
            s_map[s[l]] -= 1
            # if that makes the value 0, pop it
            if s_map[s[l]] == 0:
                s_map.pop(s[l])

            # advance l pointer
            l += 1
            # advance r pointer
            r += 1
            # check to make sure r is still in range
            if r < len(s):
                s_map[s[r]] += 1

        return res
