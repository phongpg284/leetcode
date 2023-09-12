class Solution:
    def minDeletions(self, s: str) -> int:
        res = 0
        # Map to store frequency of characters
        groups = Counter(s)
        
        # Sort frequency
        freq = groups.values()
        freq = sorted(freq, reverse=True)
        
        temp = freq[0]
        # Find out number of delete operation to make sure this freq[] has no duplicate frequency
        # temp is the previous frequency that next frequency need to be lower than this value by 1
        for i in range(1, len(freq)):
            if freq[i] >= temp:             # Current freq is >= than prev value         
                if temp == 0:               # if prev already 0, delete this frequency
                    temp = 1
                temp -= 1
                res += freq[i] - temp       # Add delete operation
            else: 
                temp = freq[i]              # Current fre is < than prev value, so no delete operation need, just update temp
        return res 