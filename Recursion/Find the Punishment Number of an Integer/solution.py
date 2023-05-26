class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            sum = str(i * i)
            if self.check(i, sum, 0):
                result += i * i
        return result
    
    '''
    Check if punishment number 
    '''
    def check(self, n, str, cur):
        if cur == n and (len(str) == 0 or int(str) == 0):
            return True
        for i in range(1, len(str) + 1):
            if cur == n and (len(str) == 0 or int(str) == 0):
                return True
            elif cur < n:
                temp = self.check(n, str[i:], cur + int(str[:i]))
                if temp is True:
                    return True
        return False
                
                
        