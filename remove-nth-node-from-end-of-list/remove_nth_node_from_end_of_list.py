from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_node = head #node previous to the one that has to be deleted
        last_node = head # the last node in the list

        # moving last_node n steps ahead
        while n > 0:
            last_node = last_node.next
            n -= 1

        # if the length og the list is the same as n - start the list from the second node
        if not last_node:
            return head.next

        # moving "the window" between prev and last nodes to the end
        while last_node.next:
            last_node = last_node.next
            prev_node = prev_node.next

        prev_node.next = prev_node.next.next

        return head
