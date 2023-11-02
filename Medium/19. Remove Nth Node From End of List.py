# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lists = []
        curr = head
        while curr:
            lists.append(curr)
            curr = curr.next
        if len(lists) == n:
            head = head.next
        elif n == 1:
            lists[len(lists)-n-1].next = None
        else:
            lists[len(lists)-n-1].next = lists[len(lists)-n+1]
        return head