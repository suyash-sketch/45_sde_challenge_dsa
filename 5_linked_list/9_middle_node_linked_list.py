from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        node_len = 0

        while curr != None:
            node_len+=1
            curr = curr.next
        
        # print(node_len)
        middle = node_len // 2
        # print(middle)

        curr = head
        while middle > 0:
            curr = curr.next
            middle -=1
        
        return curr


start = ListNode(10)
start.next = ListNode(20)
start.next.next = ListNode(30)
start.next.next.next = ListNode(40)
start.next.next.next.next = ListNode(50)
start.next.next.next.next.next = ListNode(60)

print(start.val, end='->')
print(start.next.val, end='->')
print(start.next.next.val,end='->')
print(start.next.next.next.val, end='->')
print(start.next.next.next.next.val, end='->')
print(start.next.next.next.next.next.val, end='->')
print(None)

sol = Solution()
middle = sol.middle_node(start)

print(middle.val)