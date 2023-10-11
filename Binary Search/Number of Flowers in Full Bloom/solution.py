class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(flowers)
        start = sorted([start for start, end in flowers])
        end = sorted([end for start, end in flowers])
        res = []

        def binary_search(arr, target):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target and (mid == n - 1 or arr[mid + 1] > arr[mid]):
                    return mid + 1
                elif arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        # Number of flowers have bloomed - number of flowers have ended is the result of each time
        for time in people:
            res.append(binary_search(start, time) - binary_search(end, time - 1))

        return res

# Python way to do things 
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]

            