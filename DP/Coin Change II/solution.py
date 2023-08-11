class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
            
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        
        def recur(balance, index):
            if dp[index][balance] > -1:
                return dp[index][balance]
                
            temp = 0
            for i in range(index, n):
                if balance >= coins[i]:
                    if balance == coins[i]:
                        temp += 1
                    else:
                        temp += recur(balance - coins[i], i)
            dp[index][balance] = temp
            return temp
        return recur(amount, 0)
