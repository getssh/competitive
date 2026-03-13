class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        left = 0
        right = k - 1
        freq = {}

        cur_sum = sum(nums[:k])

        for i in range(right+1):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        if len(freq) == k:
            res = cur_sum
        
        for right in range(right, len(nums)):
            if right < len(nums)-1:
                if nums[right+1] in freq:
                    freq[nums[right+1]] += 1
                    cur_sum += nums[right+1]
                else:
                    freq[nums[right+1]] = 1
                    cur_sum += nums[right+1]
            
            if nums[left] in freq and freq[nums[left]] > 1:
                freq[nums[left]] -= 1
                cur_sum -= nums[left]
            elif nums[left] in freq and freq[nums[left]] == 1:
                cur_sum -= nums[left]
                del freq[nums[left]]

            if len(freq) == k:
                if cur_sum > res:
                    res = cur_sum
                     
            left += 1
        return res