class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def recursion(n,l,r,str):
            if(l == r and n == r):
                ans.append(str)
            if(l<n):
                recursion(n,l+1,r,str+'(')
            if(r<n and r<l):
                recursion(n,l,r+1,str+')')
        recursion(n,0,0,'')
        return ans