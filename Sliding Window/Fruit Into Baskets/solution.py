class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        arr = []
        temp = -1
        temp_count = 0
        for num in fruits:
            if num != temp:
                if temp != -1:
                    arr.append((temp, temp_count))
                temp = num
                temp_count = 0
            temp_count += 1
        arr.append((temp, temp_count))

        if len(arr) == 1:
            return arr[0][1]

        start, end = 0, 1
        total = arr[start][1]
        res = total
        s = [arr[start][0], arr[end][0]]

        while end < len(arr):
            if arr[end][0] not in s:
                start = end - 1
                total = arr[start][1]
                s = [arr[start][0], arr[end][0]]
            total += arr[end][1]
            end += 1
            res = max(res, total)

        return res
