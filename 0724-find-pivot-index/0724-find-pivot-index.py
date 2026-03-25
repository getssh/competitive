class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        prefix = 0
        
        for i in range(len(nums)):
            prefix += nums[i]
            if right_sum - prefix == left_sum:
                return i
            left_sum = prefix
        
        return -1