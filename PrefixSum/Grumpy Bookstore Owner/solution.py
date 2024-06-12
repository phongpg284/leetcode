class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = 0
        n = len(customers)
        prefix = [0] * (n + 1)
        hold_time = 0

        for i in range(n):
            if not grumpy[i]:
                res += customers[i]
            prefix[i + 1] = prefix[i] + (customers[i] if grumpy[i] else 0)

            if i >= minutes - 1:
                hold_time = max(
                    hold_time, prefix[i + 1] - prefix[i + 1 - minutes])

        return res + hold_time
