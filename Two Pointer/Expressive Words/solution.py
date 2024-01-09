class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        main = self.extract_word(s)
        n = len(main)
        res = 0
        for word in words:
            extract = self.extract_word(word)

            if len(extract) == n:
                is_stretch = True
                for i in range(n):
                    if extract[i][0] != main[i][0]:
                        is_stretch = False
                        continue

                    count_t = extract[i][1]
                    count_main = main[i][1]
                    if count_t > count_main or (count_main == count_t + 1 and count_t == 1):
                        is_stretch = False
                        continue
                if is_stretch:
                    res += 1
        return res

    def extract_word(self, word):
        cur = ''
        count = 0
        store = []
        for c in word:
            if c != cur:
                if cur != '':
                    store.append((cur, count))
                cur = c
                count = 1
            else:
                count += 1
        store.append((cur, count))
        return store
