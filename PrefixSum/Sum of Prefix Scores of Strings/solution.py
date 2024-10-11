class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        store = defaultdict(int)
        res = []

        for word in words:
            temp = ''
            for c in word:
                temp += c
                store[temp] += 1

        for word in words:
            temp = ''
            count = 0
            for c in word:
                temp += c
                count += store[temp]
            res.append(count)

        return res
