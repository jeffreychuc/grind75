from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP problem, we want to work bottom up.
        # first allocate the cache
        cache = [float("inf")] * (amount + 1)
        # to make amount 0 it takes 0 coins
        cache[0] = 0

        # calculate each amount, range is non inclusive so amount + 1
        for a in range(amount + 1):
            # calculate for each coin
            for c in coins:
                # if the amount is negative we move on
                # this is why the final check checks to see if the cache[amount] == float("inf") because
                # if the amount was negative we would skip over it
                if a - c >= 0:
                    cache[a] = min(cache[a], 1 + cache[a - c])

        return cache[amount] if cache[amount] != float("inf") else -1
