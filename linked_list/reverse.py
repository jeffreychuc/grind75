from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # set previous node to None, theres no previous node at the start of
    # the LL
    prev = None
    # set the current node to the head of the LL
    curr = head

    # while a current node is available.  when curr = None that means we reached the end of the LL
    while curr:
        # save the next node
        nex = curr.next

        # set current.next to the previous node to reverse the connection
        curr.next = prev

        # the new previous node is now the current node
        prev = curr

        # now we advance current to the next node we saved at the start
        curr = nex

    # curr will === none when it ends the while loop, so return prev
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
