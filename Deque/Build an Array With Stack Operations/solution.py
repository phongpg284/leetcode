class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        index = 0
        for i in range(1, n + 1):
            res.append('Push')
            if i == target[index]:
                if index == len(target) - 1:
                    return res
                else:
                    index += 1
            else:
                res.append('Pop')
        return res