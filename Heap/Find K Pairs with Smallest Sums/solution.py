class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        m = len(nums1)
        n = len(nums2)
        visited = set()
        visited.add((0, 0))
        stash = [((nums1[0] + nums2[0]), (0,0))]

        '''
            Check if next i + 1 or j + 1 item not visited then push to heap
        '''
        while k and len(stash) > 0:
            _, (i, j) = heappop(stash)
            res.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(stash, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heappush(stash, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            
            k -= 1
        return res