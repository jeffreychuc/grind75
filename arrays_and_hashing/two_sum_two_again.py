from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -= 1


print(two_sum([2, 7, 11, 15], 9))
