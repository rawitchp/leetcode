# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recursion(root,min_val,max_val):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            l = recursion(root.left,min_val,root.val)
            r = recursion(root.right,root.val,max_val)
            return l and r
        return recursion(root,float('-inf'),float('inf'))