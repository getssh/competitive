class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_val = sum(nums[0:k])
        res = cur_val

        for i in range(k, len(nums)):
            cur_val += nums[i] - nums[i-k]
            
            if cur_val > res:
                res = cur_val

        return res/k