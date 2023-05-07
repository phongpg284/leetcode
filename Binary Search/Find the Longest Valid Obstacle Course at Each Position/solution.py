class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = []
        result = []


        '''
        Find index of first obstacle > target
        '''
        def binary_search(dp, target):
            start = 0
            end = len(dp) - 1

            while(start < end):
                middle = (start + end) // 2
                if dp[middle - 1] <= target and dp[middle] > target:
                    return middle
                if dp[middle] <= target:
                    start = middle + 1
                else:
                    end = middle - 1
            return start
        

        '''
        If obstacle < last item of dp -> insert
        
        Else binary search to replace
        '''              
        for obstacle in obstacles:
            if len(dp) == 0:
                result.append(1)
                dp.append(obstacle)
            else:
                if obstacle >= dp[-1]:
                    dp.append(obstacle)
                    result.append(len(dp))
                else:
                    index = binary_search(dp, obstacle)
                    dp[index] = obstacle
                    result.append(index + 1)
                    
        return result