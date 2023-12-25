class Solution:
    def minOperations(self, s: str) -> int:
        one = 0
        zero = 0
        prev_one = 0
        prev_zero = 0
        if s[0] == '0':
            one = 1
        else:
            zero = 1

        for i in s:
            if i == '0':
                one = prev_zero + 1
                zero = prev_one
            else:
                zero = prev_one + 1
                one = prev_zero
            prev_one = one
            prev_zero = zero

        return min(zero, one)
