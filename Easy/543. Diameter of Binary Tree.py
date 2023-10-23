# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursion(root):
            if(not root):
                return [-1,-1]
            l = recursion(root.left)
            r = recursion(root.right)
            max_l = max(l[0] + 1,l[1] + 1)
            min_l = min(l[0],l[1])
            max_r = max(r[0] + 1,r[1] + 1)
            min_r = min(r[0],r[1])
            if max_l > max_r:
                if min_l-1 > max_r:
                    return [max_l,min_l-1]
                else:
                    return [max_l,max_r]
            if max_r > max_l:
                if min_r-1  > max_l:
                    return [max_r,min_r-1]
                else:
                    return [max_l,max_r]
            return [max_l,max_r]
        ans = recursion(root)
        return ans[0]+ans[1]