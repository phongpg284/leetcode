class Solution:
    def checkValidString(self, s: str) -> bool:
        open_parent = deque()
        asterisk = deque()

        for i, c in enumerate(s):
            if c == '(':
                open_parent.append(i)
            elif c == ')':
                if open_parent:
                    open_parent.pop()
                elif asterisk:
                    asterisk.pop()
                else:
                    return False
            else:
                asterisk.append(i)

        while open_parent and asterisk:
            top_parent_index = open_parent.pop()
            top_asterisk_index = asterisk.pop()
            if top_parent_index > top_asterisk_index:
                return False

        return len(open_parent) == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
