class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        r, c = self.get_pos(target[0])
        return self.lookup(0, 0, r, c, target, 0)

    def get_pos(self, c):
        i = ord(c) - ord("a")
        return i // 5, i % 5

    def lookup(self, r1, c1, r2, c2, target, i):
        if r2 < r1:
            return "U" + self.lookup(r1 - 1, c1, r2, c2, target, i)
        if c2 < c1:
            return "L" + self.lookup(r1, c1 - 1, r2, c2, target, i)
        if r2 > r1:
            return "D" + self.lookup(r1 + 1, c1, r2, c2, target, i)
        if c2 > c1:
            return "R" + self.lookup(r1, c1 + 1, r2, c2, target, i)

        if i + 1 >= len(target):
            return "!"
        next_r, next_c = self.get_pos(target[i + 1])
        return "!" + self.lookup(r1, c1, next_r, next_c, target, i + 1)
