from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1 or not list2:
        return list1 if not list2 else list2
    head = None
    curr = None
    p = None
    q = None
    # init comp
    if list1.val < list2.val:
        head = list1
        curr = list1
        p = curr.next
        q = list2
    else:
        head = list2
        curr = list2
        p = list1
        q = curr.next
    while p and q:
        if p.val < q.val:
            curr.next = p
            p = p.next
        else:
            curr.next = q
            q = q.next
        curr = curr.next

    if p is None and q:
        while q:
            curr.next = q
            curr = curr.next
            q = q.next
    if q is None and p:
        while p:
            curr.next = p
            curr = curr.next
            p = p.next
    return head


one = ListNode(1)
two = ListNode(2)
one.next = two
four = ListNode(4)
two.next = four

one_two = ListNode(1)
three_two = ListNode(3)
one_two.next = three_two
four_two = ListNode(4)
three_two.next = four_two

res = merge_two_lists(one, one_two)
while res:
    print(res.val)
    res = res.next
