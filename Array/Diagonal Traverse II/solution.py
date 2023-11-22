class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        slots = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j >= len(slots):
                    slots.append([])
                slots[i + j].append(nums[i][j])
        
        for slot in slots:
            res += slot[::-1]
        return res