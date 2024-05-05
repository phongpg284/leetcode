class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        store = defaultdict(int)
        n = len(word)
        max_freq = 0
        for i in range(0, n, k):
            sub = word[i:i + k]
            store[sub] += 1
            if store[sub] > max_freq:
                max_freq = store[sub]
        return len(word) // k - max_freq
