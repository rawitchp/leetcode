# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        curr = ans
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.sort()
        for i in nums:
            curr.val = i
            curr = curr.next
        return ans