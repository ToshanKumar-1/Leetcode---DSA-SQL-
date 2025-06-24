# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        ln = 0
        temp = head
        while temp and temp.next:
            ln += 1
            temp = temp.next
        ln += 1

        if ln == n:
            return head.next

        temp = head
        
        for i in range(ln - n - 1):
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
        return head
        