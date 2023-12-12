class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        d = Counter(nums)
        roots = [n for n in d if not d[n - 1]]
        for r in roots:
            for i in reversed(range(r, r + k)):
                if d[i] < d[r]:
                    return False
                d[i] -= d[r]
                if not d[i] and d[i + 1]:
                    roots.append(i + 1)
        return True