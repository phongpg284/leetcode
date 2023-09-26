class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        res = []
        visited = set()

        for c in s:
            count[c] -= 1
            if c not in visited:
                while res and c < res[-1] and count[res[-1]] > 0:
                    visited.remove(res.pop())
                visited.add(c)
                res.append(c)
        return ''.join(res)