class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        i = 0
        while i < n:
            if s[i] == s[i-1]:
                valid = False
                for j in range(-1, n):
                    if (j == -1 or s[i] != s[j]) and (j == n-1 or s[i] != s[j+1]):
                        s = s[:j+1] + s[i] + s[j+1:]
                        if j > i:
                            s = s[:i] + s[i+1:]
                        else:
                            s = s[:i+1] + s[i+2:]
                        valid = True
                        break;
                if not valid: 
                    return ""
                i -= 1
            i += 1
        return s