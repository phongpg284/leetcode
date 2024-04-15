class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(s, res, [])
        return res

    def helper(self, s, res, cur):
        if not s:
            res.append(cur[::])
            return

        for i in range(1, len(s) + 1):
            sub = s[:i]
            if self.is_palindrome(sub):
                s = s[i:]
                cur.append(sub)
                self.helper(s, res, cur)
                s = sub + s
                cur.pop()

    def is_palindrome(self, s):
        return s == s[::-1]
