class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        unfair = 0
        return self.giveCookies(cookies, 0, children, k, unfair)
    
    def giveCookies(self, cookies, index, children, k, unfair):
        temp = float('inf')
        for i in range(k):
            new_child = children[::]
            new_child[i] += cookies[index]
            new_unfair = unfair if new_child[i] < unfair else new_child[i]
            if new_unfair < temp:
                if index + 1 < len(cookies):
                    temp = min(temp, self.giveCookies(cookies, index + 1, new_child, k, new_unfair))
                else:
                    temp = new_unfair
        return temp
