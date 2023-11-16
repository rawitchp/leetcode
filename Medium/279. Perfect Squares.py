class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize a list to store the least number of perfect square numbers that sum to the index i
        dp = [0] + [float('inf')] * n
        
        # Iterate through all numbers from 1 to n
        for i in range(1, n + 1):
            # Iterate through all possible perfect square numbers that are less than or equal to i
            for j in range(1, int(i ** 0.5) + 1):
                # Update the least number of perfect square numbers that sum to i
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        # Return the least number of perfect square numbers that sum to n
        return dp[n]