class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n %4 != 0:
                return False
            n //= 4
        return True
    

# Math solution 
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log2(n) % 2 == 0
    
# Bitmask solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
    