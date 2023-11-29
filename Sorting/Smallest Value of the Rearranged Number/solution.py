class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        
        digits = [0] * 10
        sign = num > 0
        num = abs(num)

        while num > 0:
            digits[num % 10] += 1
            num = num // 10
        res = ''
        if sign:
            i = 1
            while i < 10:
                if digits[i] > 0:
                    res += str(i)
                    digits[i] -= 1
                    break
                i += 1
            res += '0' * digits[0]

            while i < 10:
                res += str(i) * digits[i]
                i += 1
        else:
            for i in range(9, -1, -1):
                res += str(i) * digits[i]
        
        return int(res) * (1 if sign else -1)
            
            