class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        for i in range(n):
            xor = arr[i]
            for j in range(i + 1, n):
                xor ^= arr[j]
                if xor == 0:
                    res += j - i

        return res
