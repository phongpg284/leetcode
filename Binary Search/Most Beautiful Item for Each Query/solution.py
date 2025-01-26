class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items)
        res = []

        max_beauty_at_price = []
        current_max_beauty = 0

        for price, beauty in items:
            current_max_beauty = max(current_max_beauty, beauty)
            max_beauty_at_price.append((price, current_max_beauty))

        queries = sorted((q, i) for i, q in enumerate(queries))

        res = [0] * len(queries)

        for q, i in queries:
            idx = bisect_right(max_beauty_at_price, (q, float('inf'))) - 1
            if idx >= 0:
                res[i] = max_beauty_at_price[idx][1]
            else:
                res[i] = 0

        return res
