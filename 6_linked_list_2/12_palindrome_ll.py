from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

class Solution:

    def reverse_linked_list(self, head: ListNode):
        if head is None or head.next is None:
            return head
        
        new_head = self.reverse_linked_list(head.next)

        front = head.next

        front.next = head

        head.next = None

        return new_head

    def is_palindrome(self,head: Optional[ListNode]):
        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head

        # Traverse the linked list to find the middle using slow and fast pointers
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        new_head = self.reverse_linked_list(slow.next)

        first = head
        second = new_head

        while second is not None:
            if first.val != second.val:
                self.reverse_linked_list(new_head)
                return False
            
            first = first.next
            second = second.next
        
        self.reverse_linked_list(new_head)

        return True



start = ListNode(0)
start.next = ListNode(1)
start.next.next = ListNode(2)
start.next.next.next = ListNode(2)
start.next.next.next.next = ListNode(1)
start.next.next.next.next.next = ListNode(0)

sol = Solution()
answer = sol.is_palindrome(start)

print(answer)