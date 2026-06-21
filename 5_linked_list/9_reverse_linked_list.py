from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

        
start = ListNode(10)
start.next = ListNode(20)
start.next.next = ListNode(30)
start.next.next.next = ListNode(40)
start.next.next.next.next = ListNode(50)

print(start.val, end='->')
print(start.next.val, end='->')
print(start.next.next.val,end='->')
print(start.next.next.next.val, end='->')
print(start.next.next.next.next.val, end='->')
print(None)

sol = Solution()

rev_start = sol.reverse_list(start)

print(rev_start.val, end='->')
print(rev_start.next.val, end='->')
print(rev_start.next.next.val, end='->')
print(rev_start.next.next.next.val, end='->')
print(rev_start.next.next.next.next.val, end='->')