# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # dic={}
        # while head:
        #     if dic.has_key(head.val):
        #         if dic[head.val] == 't':
        #             return True
        #     else:
        #         dic[head.val] = 't'
        #     head = head.next
        while head:
            if head.val == 't':
                return True
            else:
                head.val = 't'
            head = head.next
        return False
        