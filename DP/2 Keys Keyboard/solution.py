class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        i = 2
        while n > 1:
            if n % i == 0:
                n /= i
                result += i
            else:
                i += 1
        return result