class Solution:
    def numSteps(self, s: str) -> int:
        s = ['0'] + list(s)
        res = 0

        while not (len(s) <= 2 and s[-1] == '1'):
            i = len(s) - 1
            res += 1
            if s[i] == '0':
                s.pop()
            else:
                while s[i] != '0':
                    s[i] = '0'
                    res += 1
                    i -= 1
                s[i] = '1'
                s = s[:i + 1]    
        return res

                    