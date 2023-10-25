# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = [[p,q]]
        while queue:
            sub1,sub2 = queue.pop(0)
            if sub1 and sub2:
                if sub1.val != sub2.val:
                    return False
                queue.append([sub1.left,sub2.left])
                queue.append([sub1.right,sub2.right])
            elif not sub1 and not sub2:
                continue
            else:
                return False
        return True