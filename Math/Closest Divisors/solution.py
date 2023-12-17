class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a, b = self.helper(num + 1)
        c, d = self.helper(num + 2)
        return [a, b] if abs(a - b) < abs(c - d) else [c, d]

    def helper(self, num):
        i = math.floor(math.sqrt(num))
        while i > 0:
            if num % i == 0:
                return i, num // i
            i -= 1
