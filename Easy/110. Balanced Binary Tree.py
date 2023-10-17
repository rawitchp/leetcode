# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recursion(root,i):
            if root:
                l = recursion(root.left,i+1)
                r = recursion(root.right,i+1)
                print(l,r)
                if(l == -1 or r == -1):
                    return -1
                if(abs(l-r) >= 2):
                    return -1
                else:
                    return max(l,r)
            else:
                return i
        ans = recursion(root,0)
        
        if ans == -1: 
            return False 
        else: 
            return True

      
        

        