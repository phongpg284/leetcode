class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_bits = 0
        prev_max = -1
        cur_max = 0

        for num in nums:
            cur_bits = num.bit_count()
            if cur_bits == prev_bits:
                cur_max = max(cur_max, num)
            else:
                prev_max = cur_max
                cur_max = num

            if num < prev_max:
                return False

            prev_bits = cur_bits

        return True
