# 121. Best Time to Buy and Sell Stock
# Easy
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
#
# Constraints:
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# Initial thoughts:
# can brute force it with two pointers..

from typing import List


# the below soution is too slow for leetcode, can speed it up by using two moving pointers instead of
# checking every single value
# def max_profit(prices: List[int]) -> int:
#     res = 0
#     # start at 0 -> end
#     for i in range(len(prices)):
#         # start at i + 1 -> end
#         for j in range(i + 1, len(prices)):
#             profit = prices[j] - prices[i]
#             res = max(res, profit)
#     return res


def max_profit(prices: List[int]) -> int:
    res = 0
    # start at 0 -> end
    l = 0
    r = 1

    while r < len(prices):
        # check profit, only profitable if left price is less than right price
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            res = max(res, profit)
        else:
            l = r
        r += 1
    return res


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([1, 2]))
