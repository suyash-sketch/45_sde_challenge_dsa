class ListNode:
    def __init__(self, val=0, next=None, random=None) -> None:
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def insert_copy_inbetween(self, head: ListNode):
        temp = head
        while temp:
            next_element = temp.next
            copy = ListNode(temp.val)

            copy.next = next_element

            temp.next = copy

            temp = next_element

    def connect_random_pointers(self, head: ListNode):
        temp = head
        while temp:
            copy_node = temp.next

            if temp.random:
                copy_node.random = temp.random.next
            else:
                copy_node.random = None

            temp = temp.next.next

    def get_deep_copy_list(self, head: ListNode):
        temp = head
        dummy_node = ListNode(-1)
        res = dummy_node

        while temp:
            res.next = temp.next
            res = res.next

            temp.next = temp.next.next
            temp = temp.next

        return dummy_node.next

    def clone_ll(self, head: ListNode):
        if not head:
            return None

        self.insert_copy_inbetween(head)

        self.connect_random_pointers(head)

        return self.get_deep_copy_list(head)
