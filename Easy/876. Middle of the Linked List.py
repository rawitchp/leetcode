# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic={}
        count = 0
        while head:
            dic[count] = head
            count += 1
            head = head.next
        return dic[count//2]