class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        unfair = float('inf')
        n = len(cookies)
        
        def giveCookies(index, children):
            nonlocal unfair
            if index == n:
                unfair = min(unfair, max(children))
                return unfair

            for i in range(k):
                children[i] += cookies[index]       # pick cookies
                giveCookies(index + 1, children)
                children[i] -= cookies[index]       # unpick cookies
                if children[i] == 0:
                    break
        
        children = [0] * k
        giveCookies(0, children)
        return unfair  