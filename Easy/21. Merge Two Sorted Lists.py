# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(not list1 and not list2):
            return None
        elif(not list1):
            return list2
        elif(not list2):
            return list1
        ans = ListNode()
        cur = ans
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if(list1):
            cur.next = list1
        else:
            cur.next = list2
        return ans.next


        

        