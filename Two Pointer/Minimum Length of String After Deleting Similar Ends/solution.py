class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        left = 0
        right = n - 1

        c = None
        while left < right:
            if s[left] != s[right]:
                return right - left + 1
            while left + 1 < n and s[left + 1] == s[left]:
                left += 1
            while right - 1 >= 0 and s[right - 1] == s[right]:
                right -= 1
            left += 1
            right -= 1

        return 1 if left == right else 0
