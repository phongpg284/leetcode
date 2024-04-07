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