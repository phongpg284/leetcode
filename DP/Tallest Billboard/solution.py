'''
    dp[i] represents largest possible height of billboard with height different is i
    
    For each rod check if put it on higher side or lower side  
'''

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        total = 0
        for rod in rods:
            total += rod
        
        dp = [-1] * (total + 1)
        dp[0] = 0

        for rod in rods:
            temp = dp[::]

            for i in range(total - rod + 1):
                if temp[i] < 0:
                    continue

                dp[i + rod] = max(dp[i + rod], temp[i])
                dp[abs(i - rod)] = max(dp[abs(i - rod)], temp[i] + min(i, rod))

        return dp[0]