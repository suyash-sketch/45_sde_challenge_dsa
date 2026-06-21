from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None ):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self,l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode()
        temp = dummy
        carry = 0

        # Loop until both lists are fully traversed and no carry remains
        while (l1 is not None or l2 is not None) or carry:
            sum_val = 0

            if l1 is not None:
                sum_val+=l1.val
                l1=l1.next
            
            if l2 is not None:
                sum_val+=l2.val
                l2=l2.next
            
            # Add any carry from the previous step
            sum_val+=carry

             # Update carry for the next addition
            carry = sum_val // 10
            
            # Create a new node with the digit value (sum % 10)
            node = ListNode(sum_val % 10)

            temp.next = node

            temp = temp.next

        return dummy.next