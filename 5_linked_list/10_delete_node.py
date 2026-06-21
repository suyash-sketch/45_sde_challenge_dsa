from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None ):
        self.val = val
        self.next = next
    
class Solution:
    def delete_node(self, node : Optional[ListNode]):
        node.val = node.next.val
        node.next = node.next.next
