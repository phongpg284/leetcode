class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = float('inf')
        res = -1
        come = [0] * n
        not_come = [0] * n
        temp = 0
        for i in range(n):
            if customers[i] == 'N':
                temp += 1
                not_come[i] = temp
            else:
                not_come[i] = temp
        temp = 0
        for i in range(n - 1, -1, -1):
            if customers[i] == 'Y':
                temp += 1
                come[i] = temp
            else:
                come[i] = temp
        for i in range(n + 1):
            if i == 0:
                if come[i] < penalty:
                    penalty = come[i]
                    res = i
            elif i == n:
                if not_come[i - 1] < penalty:
                    penalty = not_come[i - 1]
                    res = i
            else:
                if (not_come[i - 1] + come[i]) < penalty:
                    penalty = not_come[i - 1] + come[i]
                    res = i
        return res