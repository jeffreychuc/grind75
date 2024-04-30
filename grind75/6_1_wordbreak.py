from typing import List
import collections


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we only want to start searching form the beginning of the word
        queue = collections.deque([s])

        # if we've already searched through a word before dont repeat the work
        visited = set()

        # while theres possible paths in the queue
        while queue:
            # remove the word to be searched on from the queue
            word = queue.popleft()

            # if we've already seen this word skip it
            if word in visited:
                continue

            # if the word is "" then we've successfully found a good word break
            if len(word) == 0:
                return True

            # add the word to visited
            visited.add(word)

            # check to see if this current slide of the string can be started with any word in the dict
            for w in wordDict:
                if word.startswith(w):
                    # add to the queue a sliced version of the string
                    queue.append(word[len(w):])

        return False
