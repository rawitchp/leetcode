# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = None
        while head:
            x = ListNode(head.val)
            x.next = ans
            ans = x
            head = head.next
        return ans