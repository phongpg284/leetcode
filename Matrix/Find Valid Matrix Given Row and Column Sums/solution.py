class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]

        i = j = 0
        while i < m and j < n:
            x = min(rowSum[i], colSum[j])
            res[i][j] = x
            rowSum[i] -= x
            colSum[j] -= x
            i += (rowSum[i] == 0)
            j += (colSum[j] == 0)
        return res
