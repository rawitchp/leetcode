class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        n = int(n)
        max_num = pow(2,31) 
        for i in range(32):
            if n >= max_num:
                n -= max_num
                count += 1
            max_num /= 2
        return count
            