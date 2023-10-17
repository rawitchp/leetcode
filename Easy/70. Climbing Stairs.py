class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic={1:1,2:2}
        def recursion(n):
            if dic.has_key(n):
                return dic[n]
            first = recursion(n-1)
            second = recursion(n-2)
            dic[n] = first + second
            return  dic[n]
        return recursion(n)