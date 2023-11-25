class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        temp = 2 if n % 2 == 1 else 1
        
        for i in range(n // 2):
            res += temp
            temp += 2
        
        return res 


class Solution:
    def minOperations(self, n: int) -> int:
        start = 2 if n % 2 == 1 else 1
        end = start + n // 2 * 2 - 2

        return (end + start) * (n // 2) // 2

