from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque()
        max_count = 0
        for char in s: 
            if char == "(":
                stack.append(char)
            if char == ")":
                if len(stack) == 0:
                    continue

                last_item = stack.pop()

                if isinstance(last_item, int):
                    if len(stack) == 0:
                        max_count = max(max_count, last_item)
                    else:
                        temp = stack.pop()
                        if temp == "(":
                            stack.append(last_item + 2)
                else: 
                    stack.append(2)
                            
                temp_sum = 0
                while len(stack) > 0:
                    temp = stack.pop()
                    if (isinstance(temp, int)):
                        temp_sum += temp
                    else: 
                        stack.append(temp)
                        break
                stack.append(temp_sum)
                max_count = max(max_count, temp_sum)
        return max_count