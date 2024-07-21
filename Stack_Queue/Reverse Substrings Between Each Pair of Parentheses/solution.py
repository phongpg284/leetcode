class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for char in s:
            if char == ')':
                rev = stack.pop()[::-1]
                stack[-1] += rev
            elif char == '(':
                stack.append('')
            else:
                stack[-1] += char

        return ''.join(stack)
