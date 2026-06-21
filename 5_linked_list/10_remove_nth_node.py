from typing import Optional

# 1 -> 2 -> 3 -> 4 -> 5 , n = 3

class ListNode:
    def __init__(self, val = 0, next = None ):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_node_from_end(self, head: Optional[ListNode], n : int):
        #if list is empty
        if head is None:
            return None

        count_len = 0
        temp = head
        while temp:
            count_len+=1
            temp = temp.next
        # print(count_len)

        # If N equals total nodes → delete head
        if count_len == n:
            return head.next
        
        res = count_len - n
        temp =head
        while temp:
            res-=1
            if res == 0:
                break
            temp = temp.next
        
        temp.next = temp.next.next

        return head


    def display_list(self, head: Optional[ListNode]):
        while head is not None:
            print(head.val, end='->')
            head = head.next
        
        print(None)



start = ListNode(10)
start.next = ListNode(20)
start.next.next = ListNode(30)
start.next.next.next = ListNode(40)
start.next.next.next.next = ListNode(50)
# start.next.next.next.next.next = ListNode(60)

sol = Solution()
sol.display_list(start)
sol.remove_nth_node_from_end(start, 2)
sol.display_list(start)