# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # Find top of the mountain
        top = self.top_mountain(mountain_arr)

        # Find by using binary search on 2 side of the mountain
        left_side = self.binary_search(mountain_arr, 0, top, target, 'left')
        if left_side != -1: return left_side
        
        right_side = self.binary_search(mountain_arr, top, n - 1, target, 'right')
        if right_side != -1: return right_side 
        
        return -1

    def top_mountain(self, mountain_arr):
        n = mountain_arr.length()
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            cur = mountain_arr.get(mid)
            prev = mountain_arr.get(mid - 1) if mid > 0 else -1
            next = mountain_arr.get(mid + 1) if mid < n - 1 else -1

            if cur > prev and cur > next:
                return mid
            elif cur > prev and cur < next:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def binary_search(self, arr, start, end, target, direction):
        while start <= end:
            mid = (start + end) // 2
            cur = arr.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                if direction == 'left':
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if direction == 'left':
                    end = mid - 1
                else:
                    start = mid + 1

        return -1