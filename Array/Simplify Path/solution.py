class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        result = ""
        stack = []
        for p in paths:
            if p == '..':
                if len(stack) > 0:
                    last = stack.pop()
                    result = result[:-(len(last) + 1)]
            elif p == '.' or p == "":
                continue
            else:
                result = result + "/" + p
                stack.append(p)
        if result == '':
            return "/" 
        return result