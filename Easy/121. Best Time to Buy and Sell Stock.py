class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        left = 0
        right = 1
        while right < len(prices):
            cur = prices[right] - prices[left]
            if prices[left] < prices[right]:
                ans = max(ans,prices[right]-prices[left])
            else:
                left = right
            right += 1
        return ans
       
            
        return 0
            
        