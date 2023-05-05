class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        result = -1

        for i in range(len(s)):
            if i < k:
                if s[i] in vowels:
                    count += 1
            else:
                if s[i] in vowels:
                    count += 1
                if s[i - k] in vowels:
                    count -= 1
            result = max(result, count)
        return result
        
