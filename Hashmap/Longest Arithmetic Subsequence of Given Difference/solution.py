class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        visited = {}
        res = 0
        source = defaultdict(list)
        for i in range(n):
            source[arr[i]].append(i)
            visited[arr[i]] = False

        for i in range(n):
            if visited[arr[i]] == False:
                temp = self.check(arr[i], 0, visited, source, difference, i)
                res = max(res, temp)
        return res
    def check(self, num, count, visited, source, dif, index):
        next = num + dif
        if next not in source:
            return count + 1
        for i in range(len(source[next])):
            if source[next][i] > index:
                visited[next] = True
                return self.check(next, count + 1, visited, source, dif, source[next][i])
        return count + 1
