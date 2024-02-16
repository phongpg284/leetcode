class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = sorted(Counter(arr).values())
        i, t = 0, 0
        while t < k:
            t += counter[i]
            i += 1

        return len(counter) - i + 1 if t > k else len(counter) - i
