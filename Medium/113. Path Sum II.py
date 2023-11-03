# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def dfs(lists,root,path_sum):
            if root and not root.left and not root.right:
                lists = lists + [root.val]
                if path_sum + root.val == targetSum:
                    ans.append(lists)
                return
            if root.left:
                dfs(lists + [root.val],root.left,path_sum + root.val)
            if root.right:
                dfs(lists + [root.val],root.right,path_sum + root.val)
            return
        dfs([],root,0)
        return ans

            
        