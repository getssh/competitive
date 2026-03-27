class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        res = [-1] * n
        
        if n < window_size:
            return res
        
        current_window_sum = sum(nums[:window_size])
        
        res[k] = current_window_sum // window_size
        
        for i in range(k + 1, n - k):
            current_window_sum = current_window_sum - nums[i - k - 1] + nums[i + k]
            res[i] = current_window_sum // window_size
            
        return res
        