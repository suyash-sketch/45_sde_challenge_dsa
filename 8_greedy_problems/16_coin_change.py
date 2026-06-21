class Solution:
    def helper(self, coins:list[int], rem:int, dp: dict):
        if rem == 0:
            return 0
        
        if rem < 0:
            return -1
        
        if rem in dp:
            return dp[rem]
        
        mini = float('inf')

        for coin in coins:
            res = self.helper(coins, rem - coin, dp)
            
            if res >= 0 and res < mini:
                mini = 1 + res

        dp[rem] = -1 if mini == float('inf') else mini
        return dp[rem]

                

    def coin_change(self, coins: list[int], amount:int) -> int:
        dp = {}

        return self.helper(coins, amount, dp)


sol = Solution()
coins = [1,2,5]
amount = 11

answer = sol.coin_change(coins, amount)
print(answer)
