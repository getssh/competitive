class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum = nums[0]
        res = [cur_sum]
        
        for i in range(1, len(nums)):
            cur_sum += nums[i]
            res.append(cur_sum)
            
        return res