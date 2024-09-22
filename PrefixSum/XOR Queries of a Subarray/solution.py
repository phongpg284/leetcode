class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [arr[0]]

        for i in range(1, len(arr)):
            prefix.append(prefix[-1] ^ arr[i])

        return [prefix[right] ^ (prefix[left - 1] if left > 0 else 0) for left, right in queries]
