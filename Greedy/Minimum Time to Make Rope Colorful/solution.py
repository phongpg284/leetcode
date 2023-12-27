class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0        
        count = 0
        total = 0
        max_val = 0
        temp_color = ''
        for i, color in enumerate(colors):
            if color != temp_color:
                if count > 1:
                    res += total - max_val
                temp_color = color
                max_val = 0
                count = 0
                total = 0
         
            count += 1
            total += neededTime[i]
            max_val = max(max_val, neededTime[i])
        if count > 1:
            res += total - max_val
        
        return res