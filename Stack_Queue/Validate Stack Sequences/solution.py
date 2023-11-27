class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque([])
        i, j = 0, 0
        m, n = len(pushed), len(popped)
        while i < m or j < n:
            if i == m and popped[j] != stack[-1]:
                return False
            if len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                stack.append(pushed[i])
                i += 1
        return True