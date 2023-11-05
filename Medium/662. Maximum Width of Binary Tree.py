# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dict = defaultdict(list)
        def recursion(root,num,h):
            dict[h].append(num)
            if not root.left and not root.right:
                return
            if root.left:
                recursion(root.left,num*2-1,h+1)
            if root.right:
                recursion(root.right,num*2,h+1)
            return
        recursion(root,1,1)
        ans = 1
        for i in dict.values():
            if len(i) == 1:
                continue
            ans = max(ans,i[len(i)-1] - i[0]+1)
        return ans