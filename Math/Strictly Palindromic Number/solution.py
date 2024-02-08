class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n + 1):
            if not self.palindrome_check(n, i):
                return False
        return True

    def palindrome_check(self, n, b):
        res = ''
        while n != 0:
            c = n % b
            res += str(c)
            n = n // b
        return res == res[::-1]
