class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        res = [0]
        letters_count = Counter(letters)
        self.helper(words, letters_count, score, 0, res, 0)
        return res[0]

    def helper(self, words, letters_count, score, cur_score, res, i):
        if i == len(words):
            res[0] = max(res[0], cur_score)
            return

        word = words[i]

        cost_chars = self.is_valid(letters_count, word)

        if cost_chars:
            for c, count in cost_chars.items():
                letters_count[c] -= count
                cur_score += score[ord(c) - ord('a')] * count

            self.helper(words, letters_count, score, cur_score, res, i + 1)

            for c, count in cost_chars.items():
                letters_count[c] += count
                cur_score -= score[ord(c) - ord('a')] * count

        self.helper(words, letters_count, score, cur_score, res, i + 1)

    def is_valid(self, letters_count, word):
        count_word = Counter(word)
        for c, count in count_word.items():
            if count > letters_count[c]:
                return None
        return count_word
