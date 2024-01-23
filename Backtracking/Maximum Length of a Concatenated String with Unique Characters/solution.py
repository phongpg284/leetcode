class Solution:
    def maxLength(self, arr: List[str]) -> int:
        s = set()
        return self.helper(arr, s, -1)

    def helper(self, arr, s, i):
        n = len(arr)
        if i == n:
            return len(s)

        word = arr[i]
        if i > -1:
            for index, c in enumerate(word):
                if c in s:
                    for j in range(index):
                        s.remove(word[j])
                    return 0
                s.add(c)

        res = 0
        for j in range(i, n):
            t = self.helper(arr, s, j + 1)
            res = max(res, t)

        if i > -1:
            for c in word:
                s.remove(c)

        return res
