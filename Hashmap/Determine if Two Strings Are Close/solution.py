class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        x = Counter(word1)
        y = Counter(word2)

        if set(x.keys()) != set(y.keys()):
            return False

        return sorted(x.values()) == sorted(y.values())
        