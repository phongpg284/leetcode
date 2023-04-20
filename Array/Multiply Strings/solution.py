class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        len_1 = len(num1)
        len_2 = len(num2)
        count = 0
        res = ""
        for i in range(len_1 + len_2):
            cur = 0
            for j in range(0, i + 1):
                if j >= len_1 or (i-j) >= len_2:
                    continue
                cur += int(num1[j]) * int(num2[i-j])

            cur += count
            count = cur // 10
            res += str(cur % 10)
        while res[-1] == "0" and len(res) > 1:
            res = res[:len(res) - 1]
        return res[::-1]