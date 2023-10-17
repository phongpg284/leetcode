class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = {}
        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]
            if left != -1:
                if left in parent or (i in parent and parent[i] == left):
                    return False
                parent[left] = i
            if right != -1:
                if right in parent or (i in parent and parent[i] == right):
                    return False
                parent[right] = i
        if len(parent.keys()) != n - 1:
            return False
        
        for i in range(n):
            if i not in parent: 
                visited = [False] * n
                if not self.dfs(visited, i, leftChild, rightChild):
                    return False
                if not False in visited:
                    return True
        return False

    def dfs(self, visited, node, leftChild, rightChild):
        if visited[node]:
            return False
        visited[node] = True
        temp = True
        if leftChild[node] != -1:
            temp = self.dfs(visited, leftChild[node], leftChild, rightChild)
        if temp is False:
            return False
        if rightChild[node] != -1:
            temp = self.dfs(visited, rightChild[node], leftChild, rightChild)
        if temp is False:
            return False
        return True
        