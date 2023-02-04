class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        result = ''
        for i in range(len(x)-1,-1,-1):
            if i == 0 and x[i] == '-':
                result = '-' + result
            else :
                result += x[i]
        result = int(result)
        if result > pow(2,31)-1 or result < -(pow(2,31)):
            return 0
        return result