class Solution:
    def maxScore(self, s: str) -> int:
        res = -1
        temp = 0
        total_one = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                temp += 1
            else:
                total_one += 1
                temp -= 1
            res = max(res, temp)

        return total_one + res + (1 if s[-1] == '1' else 0)
