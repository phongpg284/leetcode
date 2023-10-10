class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start, end = nums[0], nums[0]
        res = []
        for num in nums[1:]:
            if num == end + 1:
                end = num 
            else:
                if end != start:
                    res.append(str(start) + "->" + str(end))
                else:
                    res.append(str(end))
                start = num
                end = num
        if end != start:
            res.append(str(start) + "->" + str(end))
        else:
            res.append(str(end))
        return res

