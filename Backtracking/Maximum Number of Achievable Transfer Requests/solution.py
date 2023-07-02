class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = [0]
        status = [0] * n
        self.solve(requests, status, 0, n, 0, res)
        return res[0]

    def solve(self, requests, status, start, n, count, res):
        if start == len(requests):
            for i in range(n):
                if status[i] != 0:
                    return
            res[0] = max(res[0], count)
            return

        status[requests[start][0]] -= 1
        status[requests[start][1]] += 1

        self.solve(requests, status, start + 1, n, count + 1, res)

        status[requests[start][0]] += 1
        status[requests[start][1]] -= 1

        self.solve(requests, status, start + 1, n, count, res)
