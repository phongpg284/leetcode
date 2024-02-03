class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or (len(token) > 1 and token[0] == '-'):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    combine = first + second
                elif token == '-':
                    combine = first - second
                elif token == '*':
                    combine = first * second
                else:
                    if first > 0 and second > 0:
                        combine = first // second
                    elif first < 0 and second < 0:
                        combine = abs(first) // abs(second)
                    else:
                        combine = -(abs(first) // abs(second))
                stack.append(combine)
        return stack[0]
