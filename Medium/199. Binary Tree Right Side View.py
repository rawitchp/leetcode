# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = [[root]]
        while q:
            f = q.pop(0)
            pushed = False
            new_q = []
            for i in f:
                if i:
                    if not pushed:
                        ans.append(i.val)
                        pushed = True
                    new_q.append(i.right)
                    new_q.append(i.left)
            if len(new_q) > 0:
                q.append(new_q)
        return ans