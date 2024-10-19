class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(m):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        for i in range(n - m):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[i]) - ord('a')] -= 1
            s2_count[ord(s2[i + len(s1)]) - ord('a')] += 1

        return s1_count == s2_count
