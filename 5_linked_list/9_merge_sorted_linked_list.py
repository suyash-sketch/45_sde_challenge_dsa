from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def merge_two_list(self,list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy_node = ListNode(-1)
        temp = dummy_node

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next
        
        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2
        
        return dummy_node.next

    def display_list(self, head: Optional[ListNode]):
        while head is not None:
            print(head.val, end='->')
            head = head.next
        
        print(None)


l1 = ListNode(10)
l1.next = ListNode(30)
l1.next.next = ListNode(50)
l1.next.next.next = ListNode(70)

print(l1.val, end='->')
print(l1.next.val, end='->')
print(l1.next.next.val,end='->')
print(l1.next.next.next.val, end='->')
print(None)

l2 = ListNode(20)
l2.next = ListNode(40)
l2.next.next = ListNode(60)

print(l2.val, end='->')
print(l2.next.val, end='->')
print(l2.next.next.val,end='->')
print(None)

sol = Solution()
merged_list_start = sol.merge_two_list(l1,l2)
print(merged_list_start.val)
sol.display_list(merged_list_start)