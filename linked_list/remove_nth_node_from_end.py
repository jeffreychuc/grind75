# 19. Remove Nth Node From End of List
# Medium
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
# Follow up: Could you do this in one pass?

# Initial Thoughts:
# need to know length of the LL to be able to get the nth from the end
# one pass to get length and then one pass to get to nth from end?

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head is None:
        return None
    ll_length = 0
    curr = head
    while curr:
        ll_length += 1
        curr = curr.next
    # 1,2,3,4,5,6,7,8
    # n = 3 so remove # 6
    # ll_length = 8
    # node_to_remove = 8 - 2
    node_to_remove = ll_length - n
    curr_count = 0
    curr = head
    prev = None
    while curr:
        if curr_count == node_to_remove:
            # logic to remove node
            # happy case with a removal of a node in the middle of a list
            if prev is not None:
                prev.next = curr.next
                curr = None
            elif prev is None and ll_length == 1:
                # if prev is None and length is 1 special case
                curr.next = None
                head = None
            else:
                # reassign head to next node
                head = curr.next
                curr.next = None
            return head
        curr_count += 1
        prev = curr
        curr = curr.next
