# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next is None:
            return head

        # print('1', head.val)
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        # print('2', p.val, head.val)
        return pj


