class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child_employee = dict()
        visited = [False] * n
        if n == 1:
            return 0
        for i, m in enumerate(manager):
            if m != -1:
                if m not in child_employee:
                    child_employee[m] = [i]
                else:
                    child_employee[m].append(i)
        result = 0
        visited[headID] = True
        for child in child_employee[headID]:
            if visited[child] is False:
                result = max(result, self.traverse(visited, child, child_employee, informTime[headID], informTime))
        return result
    
    def traverse(self, visited, node, child_employee, time, informTime):
        visited[node] = True
        if node not in child_employee:
            return time
        temp = time + informTime[node]
        max_temp = temp
        for child in child_employee[node]:
            if visited[child] is False:
                max_temp = max(max_temp, self.traverse(visited, child, child_employee, temp, informTime))
        return max_temp
