class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        map = [0] * length
        for i in range(length - 1, -1, -1):
            map[i] = [0] * length
            for j in range(i, length):
                if i == j:
                    map[i][j] = 1
                else:
                    if s[i] == s[j]:
                        map[i][j] = map[i+1][j-1] + 2
                    else:
                        map[i][j] = max(map[i+1][j], map[i][j-1])
        return map[0][length-1]