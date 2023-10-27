class Solution:
    def longestPalindrome(self, s: str) -> str:
        even = self.longestPalindromeEven(s)
        odd = self.longestPalindromeOdd(s)
        return odd if len(odd) > len(even) else even

    def longestPalindromeOdd(self, s):
        n = len(s)
        result = 1
        start = 0
        end = 0
        for i in range(n - 1):
            step = 1
            count = 1
            while step < n / 2:
                if i+ step < n and i - step >= 0 and s[i + step ] == s[i - step]:
                    count += 2
                    step += 1
                else:
                    break
                
            if count > result:
                result = count
                start = i - (step -1)
                end = i + (step -1 )
        return s[start: end +1]

    def longestPalindromeEven(self, s):
        n = len(s)
        result = 0
        start = 0
        end = 0
        for i in range(n - 1):
            step = 1
            count = 1

            if s[i+1] != s[i]:
                continue
            while step < n / 2:
                if i + 1 + step < n and i - step >= 0 and s[i + 1  + step ] == s[i - step]:
                    count += 2
                    step += 1
                else:
                    break                
            if count > result:
                result = count
                start = i - (step -1)
                end = i  + 1 + (step -1 )
        return s[start: end +1]