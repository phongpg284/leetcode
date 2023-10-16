class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res = [0] + res + [0]
            temp = []
            for j in range(len(res) - 1):
                temp.append(res[j] + res[j + 1])
            res = temp
        return res