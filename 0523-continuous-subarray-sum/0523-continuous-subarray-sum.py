class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = [0] * len(nums)
        reminder_sum = [0] * len(nums)

        pre_sum[0] = nums[0]
        reminder_sum[0] = nums[0] % k

        freq = {0: -1}

        if reminder_sum[0] not in freq:
            freq[reminder_sum[0]] = 0

        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i-1] + nums[i]
            reminder_sum[i] = pre_sum[i] % k

            if reminder_sum[i] in freq:
                if i - freq[reminder_sum[i]] >= 2:
                    return True
            else:
                freq[reminder_sum[i]] = i
        
        return False
