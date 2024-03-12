from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        # get the next node
        next = curr.next
        # reverse the pointer for current to point to previous node
        curr.next = prev
        # update the previous node to the current node
        prev = curr
        # move to the next node in the list
        curr = next
    return prev


one = ListNode(1)
two = ListNode(2)
one.next = two
three = ListNode(3)
two.next = three
four = ListNode(4)
three.next = four

res = reverse_list(one)
while res:
    print(res.val)
    res = res.next
