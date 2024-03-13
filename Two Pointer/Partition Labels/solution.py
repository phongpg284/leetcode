class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        suffix_end = {s[i]: i for i in range(n)}
        res = []
        i = 0
        while i < n:
            j = i
            max_end = suffix_end[s[j]]
            while j < max_end:          # move right pointer to max end character of current partition
                j += 1
                max_end = max(max_end, suffix_end[s[j]])
            res.append(j - i + 1)
            i = j + 1

        return res
