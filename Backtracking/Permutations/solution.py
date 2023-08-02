class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * n
        res = []
        
        def backtrack(temp):
            # Form a permutation
            if len(temp) == n:
                res.append(temp[:])
                return

            for i in range(n):
                # Recur on not pick nums 
                if not visited[i]:
                    # Pick into current temp permutation
                    visited[i] = True
                    temp.append(nums[i])
                    
                    backtrack(temp)
                    
                    # Unpic from current temp permutation
                    visited[i] = False
                    temp.pop()
        
        backtrack([]) 
        return res