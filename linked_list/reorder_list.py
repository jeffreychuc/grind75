# 143. Reorder List
# Medium
# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000
# notes:

# problem is basically telling you to merge two lists, the first half and the second half
# the second half though is reversed order
# so this problem is broken up into 3 parts
# part1: find mid point to make two lists
# part2: reverse the second half
# part3: merge the lists

# you can find the midpoint of the list using a slow and a fast pointer

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_midpoint(head: ListNode) -> ListNode:
    slow = head
    fast = head.next
    while fast is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def reverse_ll(head: ListNode) -> ListNode:
    # 1,2,3
    curr = head
    prev = None
    while curr:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n

    return prev


def reorder_list(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head:
        return None

    midpoint = find_midpoint(head)
    start_of_second_list = midpoint.next
    midpoint.next = None
    # 1,2,3  4,5,6
    second_list_reversed = reverse_ll(start_of_second_list)
    # 1,2,3  6,5,4

    # now merge the lists
    # i could probably clean this up but the logic is solid
    first_list = head
    while second_list_reversed:
        tmp_one = first_list.next
        tmp_two = second_list_reversed.next
        # 1,6
        first_list.next = second_list_reversed
        second_list_reversed.next = tmp_one
        first_list = tmp_one
        second_list_reversed = tmp_two
