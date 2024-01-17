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


# None recur
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        i = 0
        r1, c1 = 0, 0
        path = ''

        while i < len(target):
            r2, c2 = self.get_pos(target[i])
            if r2 < r1:
                path += "U"
                r1 -= 1
                continue
            if c2 < c1:
                path += "L"
                c1 -= 1
                continue
            if r2 > r1:
                path += "D"
                r1 += 1
                continue
            if c2 > c1:
                path += "R"
                c1 += 1
                continue
            path += '!'
            i += 1
        return path

    def get_pos(self, c):
        i = ord(c) - ord("a")
        return i // 5, i % 5
