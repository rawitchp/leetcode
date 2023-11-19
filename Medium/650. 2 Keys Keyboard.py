class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        dp[2] = 2
        for i in range(3,n+1):
            num = i
            max_j = 1
            for j in range(num//2,1,-1):
                if num%j == 0:
                    max_j = j
                    break
            if max_j == 1:
                dp[i] = i
            else:
                dp[i] = dp[max_j] + (i//max_j)
        return int(dp[-1])