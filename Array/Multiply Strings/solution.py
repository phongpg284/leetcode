class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        count = 0
        res = ""
        for i in range(n1 + n2):
            cur = 0
            for j in range(i + 1):
                if j < n1 and (i - j) < n2:
                    cur += int(num1[n1 - 1 - j]) * int(num2[n2 - 1 - i + j])

            cur += count
            count = cur // 10
            res += str(cur % 10)

        res = res[::-1].lstrip('0')
        return res if res else '0'
