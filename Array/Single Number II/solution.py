class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for key, count in counter.items():
            if count == 1:
                return key