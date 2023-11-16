class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [-1]
        prev = prices[0]
        ans = 0
        for i in prices[1:]:
            if i > prev and i > dp[len(dp)-1]:
                dp.append(i)
            else:
                if len(dp) > 1:
                    ans += max(dp)-prev
                prev = i
                dp = [-1]
        if len(dp) > 1:
            ans += max(dp)-prev
        return ans