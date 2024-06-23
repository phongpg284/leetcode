class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        res = 0
        inc = deque()
        dec = deque()

        for end, num in enumerate(nums):
            while inc and num < inc[-1]:
                inc.pop()
            inc.append(num)

            while dec and num > dec[-1]:
                dec.pop()
            dec.append(num)

            while dec[0] - inc[0] > limit:
                if nums[start] == inc[0]:
                    inc.popleft()
                if nums[start] == dec[0]:
                    dec.popleft()
                start += 1

            res = max(res, end - start + 1)

        return res
