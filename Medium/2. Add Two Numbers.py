# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = 0
        ans = l1
        while l1.next and l2.next:
            sum_val = l1.val + l2.val + r
            if sum_val > 9:
                r = 1
                sum_val = sum_val%10
            else:
                r = 0
            l1.val = sum_val
            l1 = l1.next
            l2 = l2.next
        sum_val = l1.val + l2.val + r
        if sum_val > 9:
            r = 1
            sum_val = sum_val%10
        else:
            r = 0
        l1.val = sum_val
        if l2.next:
            l1.next = l2.next
        while r == 1:
            if not l1.next:
                l1.next = ListNode(1)
                r = 0
            else:
                l1 = l1.next
                sum_val = l1.val + r
                if sum_val > 9:
                    r = 1
                    sum_val = sum_val%10
                else:
                    r = 0
                l1.val = sum_val
        return ans


        