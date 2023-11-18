class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        dp = defaultdict(int)
        dp[0] = 1
        def recursion(n):
            if n in dp:
                return dp[n]
            res = 9
            s = 9
            for i in range(n-1):
                res *= s
                s -= 1
            dp[n] = res + recursion(n-1)
            return dp[n]
        return recursion(n)