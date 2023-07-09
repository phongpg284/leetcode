class Solution:
    def largestVariance(self, s: str) -> int:
        count1, count2 = 0, 0
        res = 0
        chars = set(s)
        pairs = [(c1, c2) for c1 in chars for c2 in chars if c1 != c2]

        for _ in range(2):                  # Reverse and traverse again
            for (c1, c2) in pairs:          
                count1 = count2 = 0
                for char in s:
                    if char == c1:
                        count1 += 1
                    elif char == c2:
                        count2 += 1
                    else: 
                        continue
                        
                    if count1 < count2:
                        count1 = 0
                        count2 = 0
                    elif count1 > 0 and count2 > 0: 
                        res = max(res, count1 - count2)
            s = s[::-1]
        return res
