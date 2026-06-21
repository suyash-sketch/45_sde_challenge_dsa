class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotate_right(self, head: ListNode, k : int):
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length+=1

        tail.next = head

        k = k % length

        steps_to_newtail = length - k 
        new_tail = head
        for _ in range(steps_to_newtail - 1):
            new_tail = new_tail.next

        #set new head
        new_head = new_tail.next

        #break the circle
        new_tail.next = None

        return new_head
            