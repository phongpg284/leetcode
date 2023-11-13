class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a' , 'e', 'i', 'o', 'u', 'A' , 'E', 'I', 'O', 'U'])
        n = len(s)
        vowel_char = []
        vowel_pos = []
        
        for i, c in enumerate(s):
            if c in vowels:
                vowel_char.append(c)
                vowel_pos.append(i)
        
        vowel_char = sorted(vowel_char)

        if len(vowel_pos) == 0:
            return s
            
        res = list(s)

        for i, pos in enumerate(vowel_pos):
            res[pos] = vowel_char[i]
        return ''.join(res)
