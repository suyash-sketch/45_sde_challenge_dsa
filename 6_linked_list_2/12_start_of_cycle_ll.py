class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

class Solution:
    def has_cycle(self, head: ListNode):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None