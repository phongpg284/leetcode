# Normal Recursive solution
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.recur(n, k, 0, [], res)
        return res
    def recur(self, n, k, i, group, res): 
        if len(group) == k:
            res.append(group)
        for j in range(i+1, n+1):
            new_group = group[:]
            new_group.append(j)
            self.recur(n, k, j, new_group, res)


# Back track solution
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