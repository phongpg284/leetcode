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


## optimize no heap
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        chunk = freq[25] - 1                                ## each chunk consist all slot for all character -> number of chunk will be maximum frequency
        idle = chunk * n                                    ## init idle as all other slot in total - 1 chunk 

        for i in range(24, -1, -1):                         ## for every frequency, we can replace that amount of character instead of idle slot 
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)       ## result will be len(tasks) + slots that need to be idle



