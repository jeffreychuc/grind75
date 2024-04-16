from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get length with a pointer first
        # calculate middle
        # traverse to middle and return
        if not head:
            return None
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        middle = length // 2
        curr = head
        for _ in range(middle):
            curr = curr.next

        return curr


# you don't need to traverse the LL twice, keep 2 pointers, one curr, one lag.
# move lag every 2 curr moves and it should be the midpoint
class AnotherSolution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        lag = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
            if length % 2 == 0:
                lag = lag.next

        return lag
