import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))
        
        while left <= right:
            res = left * left + right * right
            
            if res == c:
                return True
            elif res < c:
                left += 1
            else:
                right -= 1
                
        return False
