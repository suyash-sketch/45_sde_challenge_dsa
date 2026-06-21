class ListNode:
    def __init__(self, val = 0, next = None, child = None):
        self.val = val
        self.next = next
        self.child = child
    
class Solution:
    ''' Merge the two linked lists in a particular
     order based on the data value '''
    def merge(self, list1: ListNode, list2: ListNode ):
        dummy = ListNode(-1)
        res = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
            
            res.next = None
        
        if list1:
            res.child = list1
        else:
            res.child = list2

        if dummy.child:
            dummy.child.next = None

        return dummy.child


    def flatten_linked_list(self,head: ListNode):

        if head is None or head.next is None:
            return head
        
        merged_head = self.flatten_linked_list(head.next)

        head = self.merge(head, merged_head)
        return head
