class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        store = {}
        palind_words = set()
        for word in words:
            if word not in store:
                store[word] = 0
            store[word] += 1
            if word == word[::-1]:
                palind_words.add(word)

        res = 0
        for word, count in store.items():
            rev = word[::-1]
            if rev in store and store[rev] > 0:
                if word != rev:
                    pairs = min(count, store[rev])
                    store[word] -= pairs
                    store[rev] -= pairs
                else:
                    pairs = count // 2
                    store[word] -= pairs * 2
                res += pairs * 4

        for word in palind_words:
            if store[word] > 0:
                res += 2
                return res
        return res
