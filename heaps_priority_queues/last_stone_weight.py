import heapq
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    # turn the list of stones into a max heap
    # python only offers a min heap so if we make
    # the values in the list negative we can make
    # a fake max heap

    if len(stones) == 1:
        return stones[0]

    fake_max_heap = [-i for i in stones]
    heapq.heapify(fake_max_heap)
    # now fake_max_heap is a max heap but every value is negative
    stone_x = None
    stone_y = None
    # while theres values in the max heap
    while fake_max_heap:
        if stone_y is None and fake_max_heap:
            stone_y = heapq.heappop(fake_max_heap) * -1
        if stone_x is None and fake_max_heap:
            stone_x = heapq.heappop(fake_max_heap) * -1

        if stone_x == stone_y:
            stone_x = None
            stone_y = None
        elif stone_x and stone_y:
            stone_y = stone_y - stone_x
            stone_x = None
            heapq.heappush(fake_max_heap, stone_y * -1)
            stone_y = None

    if stone_y is None and stone_x is None:
        return 0

    return stone_y


print(last_stone_weight([2, 7, 4, 1, 8, 1]))  # 1
