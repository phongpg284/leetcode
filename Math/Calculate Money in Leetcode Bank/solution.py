class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        left = n % 7
        start_week = (7 + 1) * 7 // 2 
        res = start_week * weeks + (7 * weeks) * (weeks - 1) // 2
        
        for i in range(left):
            res += weeks + 1 + i
        return res 