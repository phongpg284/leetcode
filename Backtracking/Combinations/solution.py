class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def recur(i, group): 
            if len(group) == k:
                res.append(group[:])
            for j in range(i, n+1):
                group.append(j)
                recur(j + 1, group)
                group.pop()
        
        recur(1, [])
        return res