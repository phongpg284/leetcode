class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = [int(revision) for revision in version1.split('.')]
        p2 = [int(revision) for revision in version2.split('.')]
        n1, n2 = len(p1), len(p2)
        n = max(n1, n2)
        for i in range(n):
            t1 = p1[i] if i < n1 else 0
            t2 = p2[i] if i < n2 else 0
            if t1 < t2:
                return -1
            if t1 > t2:
                return 1
        return 0
