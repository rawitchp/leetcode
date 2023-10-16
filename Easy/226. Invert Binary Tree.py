# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def recursion(root):
            if root:
                l = recursion(root.left)
                r = recursion(root.right)
                root.right = l
                root.left = r
                return root
            else:
                return
        return recursion(root)