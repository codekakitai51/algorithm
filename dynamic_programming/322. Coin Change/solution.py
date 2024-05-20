class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for iD in range(1, amount + 1):
            for iC in range(len(coins)):
                nextDP = iD - coins[iC]
                if nextDP >= 0:
                    dp[iD] = min(dp[iD], 1 + dp[nextDP])
        
        return dp[amount] if dp[amount] != float("inf") else -1