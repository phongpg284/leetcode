class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        
        '''
        For every k up higher, we need to pick 2 marbles adjacent to add to score 
        ---> build partition list 
        ---> sort partition to pick max and min partition count to score max and min
        '''

        if n <= 2 or n == k:
            return 0
        
        partition= [0] * (n - 1)
        for i in range(n - 1):
            partition[i] = weights[i] + weights[i + 1]

        partition.sort()

        maxP = sum(partition[n - k:])
        minP = sum(partition[:k - 1])
        return maxP - minP
