class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(i, j):
            if i == j:
                return [int(expression[i])]
            if i == j - 1 and expression[j] not in '+-*':
                return [int(expression[i: j + 1])]
            if (i, j) in memo:
                return memo[(i, j)]
            res = []
            for k in range(i, j + 1):
                ch = expression[k]
                if ch in '+-*':
                    left = dfs(i, k - 1)
                    right = dfs(k + 1, j)
                    for l1 in left:
                        for l2 in right:
                            if ch == '+':
                                res += [l1 + l2]
                            elif ch == '-':
                                res += [l1 - l2]
                            elif ch == '*':
                                res += [l1 * l2]
            memo[(i, j)] = res
            return memo[(i, j)]
        n = len(expression)
        memo = dict()
        return dfs(0, n - 1)