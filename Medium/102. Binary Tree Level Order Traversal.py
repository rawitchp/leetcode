# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = [[root]]
        ans = []
        while len(q) > 0:
            cur_l = q[0]
            next_l = []
            val_in_l = []
            for i in cur_l:
                if not i:
                    continue
                else:
                    val_in_l.append(i.val)
                    next_l.append(i.left)
                    next_l.append(i.right)
            if next_l != []:
                q.append(next_l)
            if val_in_l != []:
                ans.append(val_in_l)
            q = q[1:]
        return ans