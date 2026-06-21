from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def display_ll(self, head:ListNode):
        curr = head
        while curr is not None:
            print(curr.val, end="->")
            curr = curr.next
        
        print(None)

    def get_kth_node(self,curr: ListNode, k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        
        return curr

    def reverse_k_group(self, head: Optional[ListNode], k: int):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            prev = group_next
            curr = group_prev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        
        return dummy.next


start = ListNode(10)
start.next = ListNode(20)
start.next.next = ListNode(30)
start.next.next.next = ListNode(40)
start.next.next.next.next = ListNode(50)
start.next.next.next.next.next = ListNode(60)


sol = Solution()
sol.display_ll(start)
revered_start = sol.reverse_ll(start, k=3)
sol.display_ll(revered_start)
