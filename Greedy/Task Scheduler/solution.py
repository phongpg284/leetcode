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

# Heap implement
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-c for c in counter.values()]       ## max heap to get most frequent character
        heapq.heapify(max_heap)

        res = 0                                         ## start time
        q = deque()                                     ## queue for idle item

        while max_heap or q:                            
            res += 1

            if not max_heap:                            ## no more item in max_heap -> return queue last idle item
                res = q[0][1]
            else:
                temp = 1 + heapq.heappop(max_heap)      ## reduce counter by 1
                if temp < 0:                            
                    q.append([temp, res + n])           ## push item to idle queue, where [counter left, next time mark can reschedule]

            if q and q[0][1] == res:                    ## reach time mark which can be rescheduled
                heapq.heappush(max_heap, q.popleft()[0])
        return res


