class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            # find key point
            if nums[i] < nums[i + 1]:
                start = i + 1
                end = n - 1
                is_swap = False

                while start < end:
                    # swap key point with most recent higher
                    if is_swap is False:
                        if nums[start] > nums [i] and nums[start + 1] <= nums[i]:
                            is_swap = True
                            nums[i], nums[start] = nums[start], nums[i]
                        elif nums[end] <= nums [i] and nums[end - 1] > nums[i]:
                            is_swap = True
                            nums[i], nums[end - 1] = nums[end - 1], nums[i]
                    # reverse array after key point
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
                if is_swap is False:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                return nums
        return nums.reverse()
