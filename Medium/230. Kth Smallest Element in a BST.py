# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:      
        def recursion(root):
            if not root:
                return []
            l = recursion(root.left)
            m = [root.val]
            r = recursion(root.right)
            return l+m+r
        ans = recursion(root)
        return ans[k-1]
