class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        res = 0
        freq = {0:1}

        for i in range(len(nums)):
            nums[i] = nums[i] % 2
        
        for i in range(len(nums)):
            if nums[i] == 1:
                pre_sum += 1
            
            if pre_sum - k in freq:
                res += freq[pre_sum - k]

            freq[pre_sum] = freq.get(pre_sum, 0) + 1
        
        return res
            