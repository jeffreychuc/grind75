# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#

# First thoughts:
# we should make sorted string out of all the input phrases, the sorted string can be the keys for a hashmap.
# for each incoming string we check to see if the keys match up to an existing key, if not then we
# add it as a key.  the values in the hashmap will be the matching strings

# NB: i think this problem is really trying to find a consistent way to hash the incoming
# string as a key because ive seen other crazy solutions using ord() to hash the incoming string

from typing import List

# Time: O(NlogN)? I think its nlogn because of the sorting
# Space: O(N)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    res_map = {}
    res = []
    for s in strs:
        key = "".join(sorted(s))
        if key in res_map:
            res_map[key].append(s)
        else:
            res_map[key] = [s]
    for k in res_map.keys():
        res.append(res_map[k])

    return res


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
