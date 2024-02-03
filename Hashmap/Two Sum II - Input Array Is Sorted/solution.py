class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in store and store[t] != i:
                return [store[t] + 1, i + 1]
            store[numbers[i]] = i
