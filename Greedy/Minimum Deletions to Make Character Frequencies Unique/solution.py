class Solution:
    def minDeletions(self, s: str) -> int:
        res = 0
        groups = Counter(s)
        
        freq = groups.values()
        freq = sorted(freq, reverse=True)
        
        temp = freq[0]
        
        for i in range(1, len(freq)):
            if freq[i] >= temp:
                if temp == 0:
                    temp = 1
                temp -= 1
                res += freq[i] - temp
            else: 
                temp = freq[i]
        return res 