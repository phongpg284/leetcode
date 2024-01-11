class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        s = sorted([a, b, c])
        return [self.helper(s), s[2] - s[0] - 2]

    def helper(self, s):
        if s[0] + 1 == s[1] and s[1] + 1 == s[2]:
            return 0

        if s[1] - s[0] <= 2 or s[2] - s[1] <= 2:
            return 1

        return 2
