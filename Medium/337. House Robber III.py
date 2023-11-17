# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def recursion(root):
            if not root:
                return [0,0]
            l = recursion(root.left)
            r = recursion(root.right)
            return [root.val+l[1]+r[1],max(l)+max(r)]

        return max(recursion(root))