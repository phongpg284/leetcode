class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        cost = 0
        m, p, g = 0, 0, 0
        res = 0
        
        for i in range(n):
            cost += travel[i - 1] if i > 0 else 0
            for t in garbage[i]:
                if t == 'G':
                    res += cost - g + 1
                    g = cost
                elif t == 'P':
                    res += cost - p + 1
                    p = cost
                else:
                    res += cost - m + 1
                    m = cost

        return res
