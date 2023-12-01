class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction, reverse=True)
        temp = 0
        res = 0

        for s in satisfaction:
            if temp + s > 0:
                temp += s
                res += temp
        return res