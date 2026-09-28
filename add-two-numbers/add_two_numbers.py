from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        suma = ListNode()
        suma_head = suma
        pos = 0

        while l1 or l2:
            # If one number is shorter than another,  take the value 0 for the missing digits
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0

            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            addition = val1 + val2 + pos
            # for cases when a sum resuts in 10 or more
            if addition > 9:
                pos = 1
                addition -= 10
            else:
                pos = 0

            suma.val = addition
            # checking if we need to create one more node
            if l1 or l2 or pos == 1:
                suma.next = ListNode()
                suma = suma.next
                # in cases the lists have ended, but the last sum fos > 10
                if not l1 and not l2 and pos == 1:
                    suma.val = 1
                    return suma_head
        return suma_head
