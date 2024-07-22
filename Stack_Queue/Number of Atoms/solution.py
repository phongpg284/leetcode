class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = defaultdict(int)
        stack = [1]
        element, num = '', ''

        for i in range(len(formula) - 1, -1, -1):
            c = formula[i]
            if c.isdigit():
                num = c + num
            elif c.islower():
                element = c
            elif c.isupper():
                counts[c + element] += (int(num) if num else 1) * stack[-1]
                element, num = '', ''
            elif c == ')':
                stack.append((int(num) if num else 1) * stack[-1])
                num = ''
            elif c == '(':
                stack.pop()

        return ''.join(key + (str(freq) if freq > 1 else '') for key, freq in sorted(counts.items()))
