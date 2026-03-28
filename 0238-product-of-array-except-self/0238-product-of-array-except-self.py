import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_sum = 1
        suf_sum = [1] * len(nums)
        left = 1
        right = 1
        res = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            suf_sum[i] = nums[i] * right
            right = suf_sum[i]

        for i in range(len(nums)-1):
            res[i] = suf_sum[i+1] * left
            left *= nums[i]
        
        res[len(nums)-1] = left * 1

        return res
