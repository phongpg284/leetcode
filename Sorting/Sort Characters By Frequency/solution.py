class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        temp = sorted([(-count, c) for c, count in counter.items()])
        res = ''
        for count, c in temp:
            res += c * - count
        return res