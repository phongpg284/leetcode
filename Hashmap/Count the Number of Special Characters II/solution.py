class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        flag = defaultdict(list)
        for i in range(len(word)):
            flag[word[i]].append(i)
        res = 0

        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            if lower in flag and upper in flag and flag[lower][-1] < flag[upper][0]:
                res += 1

        return res
