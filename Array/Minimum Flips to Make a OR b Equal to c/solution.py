class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        while a or b or c: 
            last_bit_a = a & 1
            last_bit_b = b & 1
            last_bit_c = c & 1

            if last_bit_c == 1:
                if last_bit_a == 0 and last_bit_b == 0:
                    result += 1
            else: 
                result += last_bit_a + last_bit_b

            a >>= 1
            b >>= 1
            c >>= 1

        return result