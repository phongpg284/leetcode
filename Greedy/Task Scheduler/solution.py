class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        idle = {c: 0 for c in counter.keys()}
        res = 0
        total = 0

        while total < len(tasks):
            for c, count in sorted(counter.items(), key=lambda x: x[1])[::-1]:
                if counter[c] > 0 and idle[c] == 0:
                    total += 1
                    idle[c] = n + 1
                    counter[c] -= 1
                    break

            for c in idle.keys():
                if idle[c] > 0:
                    idle[c] -= 1
            res += 1
        return res
