class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord('a')] += 1

        sorted_counts = sorted(counts, reverse=True)

        res = 0
        for i, count in enumerate(sorted_counts):
            if count == 0:
                break
            res += (i // 8 + 1) * count

        return res
