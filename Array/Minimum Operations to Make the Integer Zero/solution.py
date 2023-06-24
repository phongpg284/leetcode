class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        count = 0
        while (True):
            count += 1
            total = num1 - num2 * count
            if total <= 0:
                return -1
            if self.frac(total, count):
                return count
            
    '''
        Check if number a can be turn in to sum of 2 ** i with total numbers lte count
    '''
    def frac(self, a, count):
        res = 1
        if a == 1 and count >= 2:
            return False
        
        while a > 1:
            if a % 2 == 1:
                res += 1
            a = a // 2
            if res > count:
                return False
        return True