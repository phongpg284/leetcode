class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = "1"
        for i in range(2, n + 1):
            queue = list()
            for char in result:
                if len(queue) == 0:
                    queue.append((char, 1))
                else:
                    last = queue.pop(-1)
                    if last[0] == char:
                        queue.append((char, last[1] + 1))
                    else:
                        queue.append(last)
                        queue.append((char, 1))

            result = ""
            for item in queue:
                result = result + str(item[1]) + item[0]
        return result