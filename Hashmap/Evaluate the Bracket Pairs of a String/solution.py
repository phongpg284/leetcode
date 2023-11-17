class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict()
        for key, val in knowledge:
            d[key] = val

        word = ''
        is_word_parse = False
        res = ''

        for c in s:
            if c == '(':
                is_word_parse = True
            elif c== ')':
                is_word_parse = False
                if word in d:
                    res += d[word]
                else:
                    res += '?'
                word = ''
            else:
                if is_word_parse:
                    word += c
                else:
                    res += c
        
        return res
