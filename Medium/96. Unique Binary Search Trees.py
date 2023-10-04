class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        catalans = {}
        def catalan(n,catalans):
            if(n == 0 or n == 1):
                return 1
            ans = 0
            for i in range(n):
                a = 0
                b = 0
                if(catalans.has_key(i)):
                    a = catalans[i]
                else :
                    a = catalan(i,catalans)
                    catalans[i] = a
                if(catalans.has_key(n-i-1)):
                    b = catalans[n-i-1]
                else:
                    b = catalan(n-i-1,catalans)
                    catalans[n-i-1] = b
                ans += a*b
            return ans
        return catalan(n,catalans)
