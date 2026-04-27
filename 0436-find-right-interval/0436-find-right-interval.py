class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for i in range(len(intervals)):
            starts.append([intervals[i][0], i])
        
        starts.sort()
        
        res = []
        
        for curr in intervals:
            target = curr[1]
            
            left  = 0
            right = len(starts) - 1
            found_idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if starts[mid][0] >= target:
                    found_idx = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            
            res.append(found_idx)
            
        return res