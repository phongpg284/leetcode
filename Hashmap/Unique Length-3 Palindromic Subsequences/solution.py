class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        max_pos_alphabet = [-1] * 26
        min_pos_alphabet = [float('inf')] * 26
        res = 0
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            max_pos_alphabet[index] = max(max_pos_alphabet[index], i)
            min_pos_alphabet[index] = min(min_pos_alphabet[index], i)

        for i in range(26):
            max_pos = max_pos_alphabet[i]
            min_pos = min_pos_alphabet[i]
            if max_pos > -1 and min_pos != float('inf') and min_pos != max_pos:
                res += len(set(s[min_pos+1:max_pos]))

        return res
    