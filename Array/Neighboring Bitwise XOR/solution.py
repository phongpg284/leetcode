class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        initial = 1
        current = 1
        for bit in derived:
            # switch due to a XOR b == 1 when a != b 
            if bit == 1:
                current *= -1
        if initial != current:
            return False
        return True