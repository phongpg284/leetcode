class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        remain = k % total

        for i, c in enumerate(chalk):
            if remain < c:
                return i
            remain -= c

        return 0
