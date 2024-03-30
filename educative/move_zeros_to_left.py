# Arrays: move zeros to the left
# Given an integer array, move all elements that are 0 to the left
# while maintaining the order of other elements in the array.
# The array has to be modified in-place. Try it yourself before reviewing the solution and explanation.
#

from typing import List


def move_zeros_to_left(a: List[int]):
    read = len(a) - 1
    write = len(a) - 1
    # two pointers, read and write
    # as you move backwards in the array reading from the read pointer, if the value is != 0
    # write the read value to the write index and decrement the write index
    # after youre done write 0's from the 0 index to the write index inclusive

    for w in range(read, -1, -1):
        if a[w] != 0:
            a[write] = a[w]
            write -= 1

    for w in range(write + 1):
        a[w] = 0

    return a


arr = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print(arr)
print(move_zeros_to_left(arr))
