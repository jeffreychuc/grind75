# 70. Climbing Stairs
# Easy

# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#
# 1 <= n <= 45

# Bottom up solution
def climb_stairs(n: int) -> int:
    if n == 1 or n == 2:
        return n

    cache = [0] * n
    cache[0] = 1
    cache[1] = 2
    for i in range(2, n):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n - 1]


# i still don't really get this example
# the top cache example makes sense but i still cant wrap my head around this one
def climb_stairs_top_down(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        print(i, one, two)
        temp = two
        two = two + one
        one = temp
        print(i, one, two)

    return two


print(climb_stairs(6))
print(climb_stairs_top_down(10))
