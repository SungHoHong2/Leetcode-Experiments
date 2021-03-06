# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # set the fake header and the working pointer
        head = curr = ListNode(0)
        # initialize the carry
        carry = 0
        # iterate until either l1 and l2 are empty
        while l1 or l2:
            # initialize x, y
            x = y = 0
            # if l1 is not empty assign x as l1.val
            if l1:
                x = l1.val
                l1 = l1.next
            # if l2 is not empty assign y as l2.val
            if l2:
                y = l2.val
                l2 = l2.next
            # get the sum value
            sum = x + y + carry
            # get the carry value for the next iteration
            carry = sum // 10
            # add the answer
            curr.next = ListNode(sum % 10)
            # move on to next iteration
            curr = curr.next
        # send the carry value to the next node just in case this is the end of the iteration
        if carry > 0 :
            curr.next = ListNode(carry)
        # return the result without the dummy head
        return head.next