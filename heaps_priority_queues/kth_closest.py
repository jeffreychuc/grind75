from typing import List
import heapq
import math


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    distance_map = {}
    distance_min_heap = []
    heapq.heapify(distance_min_heap)
    for x, y in points:
        d = abs((math.pow(x, 2) + math.pow(y, 2)))
        # ** 0.5 to get the sqroot we can ** 0.5 but we cant keep floats
        # in a min heap so were going to just keep the base because we
        # can just directly compare the base to figure out which one is less
        # print(d)
        arr = distance_map.get(d, [])
        arr.append([x, y])
        distance_map[d] = arr
        heapq.heappush(distance_min_heap, d)
    # print(distance_map)
    res = []
    for _ in range(k):
        d = heapq.heappop(distance_min_heap)
        # print(d)
        cord = distance_map[d].pop()
        res.append(cord)
    return res


print(k_closest([[1, 3], [-2, 2]], 1))  # [-2, 2]
