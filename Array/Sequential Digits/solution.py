class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        start, end = len(str(low)), len(str(high))
        res = []
        for i in range(start, end + 1):
            res += self.helper(i, low, high)
        return res

    def helper(self, length, low, high):
        i = 1
        res = []
        while True:
            digits = [str(j) for j in range(i, i + length)]
            if int(digits[-1]) > 9:
                return res

            s = ''.join(digits)
            val = int(s)
            if val > high:
                return res
            if val >= low:
                res.append(int(s))
            i += 1
