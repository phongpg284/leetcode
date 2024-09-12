class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (n + len(rolls)) - sum(rolls)

        if total < n or total > 6 * n:
            return []

        average = total // n
        over_count = total % n

        return [average + 1] * over_count + [average] * (n - over_count)
