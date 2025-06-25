# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        curr = dummy
        carry = 0
        t1, t2 = l1, l2

        while t1 is not None or t2 is not None:
            sm = carry
            if t1 is not None:
                sm += t1.val
                t1 = t1.next
            if t2 is not None:
                sm += t2.val
                t2 = t2.next
            
            new = ListNode(sm%10)
            carry = sm // 10
            curr.next = new
            curr = curr.next
        
        while carry > 0:
            new = ListNode(carry%10)
            carry = carry // 10
            curr.next = new
            curr = curr.next

        return dummy.next
        