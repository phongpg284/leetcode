class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low, high = 0, n 

        # mountain index satisfy arr[i-1] < arr[i] < arr[i+1]
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            elif arr[mid] < arr[mid - 1]:
                high = mid - 1
            else:
                return mid
        return mid
