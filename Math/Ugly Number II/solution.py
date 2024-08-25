class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        next_ugly = [2, 3, 5]
        increase = [1, 1, 1]
        res = [1]

        for _ in range(1, n):
            smallest = min(next_ugly)
            res.append(smallest)

            for i in range(3):
                if next_ugly[i] == smallest:
                    next_ugly[i] = primes[i] * res[increase[i]]
                    increase[i] += 1

        return res[-1]
