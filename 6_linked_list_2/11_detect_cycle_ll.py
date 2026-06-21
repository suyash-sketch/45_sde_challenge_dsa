from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        faster = head.next.next

        if not faster or not slow:
            return False

        while faster != None:
            if faster == slow:
                return True

            slow = slow.next
            faster = faster.next.next
        
        return False