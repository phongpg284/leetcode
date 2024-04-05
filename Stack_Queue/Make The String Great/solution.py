class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()

        for c in s:
            if stack and c.lower() == stack[-1].lower() and c != stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
