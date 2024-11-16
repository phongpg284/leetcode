class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        count = 1
        i = 0
        res = ''

        for i in range(n - 1):
            if word[i + 1] != word[i] or count == 9:
                res += str(count)
                res += word[i]
                count = 1
            else:
                count += 1

        res += str(count)
        res += word[n - 1]

        return res
