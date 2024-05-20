class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        deltas = [(nums[i] ^ k) - nums[i] for i in range(n)]
        deltas.sort(reverse=True)
        res = sum(nums)

        for start_ind in range(0, n - 1, 2):
            changing_delta = deltas[start_ind] + deltas[start_ind + 1]
            if changing_delta > 0:
                res += changing_delta
            else:
                break

        return res
