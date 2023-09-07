class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(1, numRows):
            prev = [0] + res[-1] + [0]
            temp = []
            for i in range(len(prev) - 1):
                temp.append(prev[i] + prev[i + 1])
            res.append(temp)
        return res