class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        
        arr = [i + 1 for i in range(n)]

        l = len(arr)
        cur = 0
        while l > 1:
            delete_index = (cur + k - 1) % l
            cur = delete_index
            arr = arr[:delete_index] + arr[delete_index + 1:]
            l = len(arr)
        return arr[0]
