class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        power = abs(n)
        ans = 1
        while power >= 1:
            if(power % 2):
                ans *= x
            power /= 2
            x *= x
        if n > 0:
            return ans
        else:
            return 1/ans