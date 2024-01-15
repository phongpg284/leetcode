class Solution:
    def minimizeResult(self, expression: str) -> str:
        n = len(expression)
        n_left = expression.index('+')
        n_right = n - 1 - n_left

        num_left = expression[:n_left]
        num_right = expression[n_left + 1:]

        min_val = float('inf')
        res = ''

        for i in range(n_left):
            for j in range(n_right):
                total = int(num_left[i:]) + int(num_right[:j + 1])
                total *= int(num_left[:i]) if i > 0 else 1
                total *= int(num_right[j + 1:]) if j < n_right - 1 else 1
                if total < min_val:
                    min_val = total
                    res = num_left[:i] + '(' + num_left[i:] + '+' + \
                        num_right[:j + 1] + ')' + num_right[j + 1:]
        return res
