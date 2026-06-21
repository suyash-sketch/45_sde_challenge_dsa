class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

class Solution:
    def get_interection_node(self, headA: ListNode, headB: ListNode):
        if not headA or not headB:
            return None
        

        currA = headA
        currB = headB
        # Loop until the pointers meet. 
        # If they don't intersect, they will both eventually become None at the same time.
        while currA != currB:

            # If currA reaches the end, jump to the head of list B. Otherwise, move forward.
            if currA is None:
                currA = headB
            else:
                currA = currA.next

            # If currB reaches the end, jump to the head of list A. Otherwise, move forward.
            if currB is None:
                currB = headB
            else:
                currB = currB.next


        return currA