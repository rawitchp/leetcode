# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursion(root):
            if(not root):
                return -1
            l = recursion(root.left) + 1
            r = recursion(root.right) + 1
            return max(l,r)
        return recursion(root) + 1