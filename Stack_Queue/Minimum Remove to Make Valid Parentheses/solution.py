class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        open_parent = 0
        for c in s:
            if c == '(':
                stack.append(c)
                open_parent += 1
            elif c == ')':
                if open_parent > 0:
                    stack.append(c)
                    open_parent -= 1
            else:
                stack.append(c)

        res = ''
        while stack:
            c = stack.pop()
            if c == '(' and open_parent > 0:
                open_parent -= 1
                continue
            res += c
        return res[::-1]
