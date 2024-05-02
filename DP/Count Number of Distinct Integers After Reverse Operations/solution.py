class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
        for num in nums:
            t = int(str(num)[::-1])
            s.add(t)
        return len(s)
