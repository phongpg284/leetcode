class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        temp1, temp2 = 0, 0
        while i >= 0 or j >= 0:
            if s[i] == '#' and i >= 0:
                temp1 += 1
                i -= 1
            else:
                if temp1 > 0 and i >= 0:
                    temp1 -= 1
                    i -= 1
                else: 
                    if t[j] == '#':
                        temp2 += 1
                    else:
                        if temp2 > 0 and j >= 0:
                            temp2 -= 1
                        else:
                            if s[i] != t[j] and i >= 0 and j >= 0:
                                return False
                            else:
                                i -= 1
                    j -= 1
        return i == j