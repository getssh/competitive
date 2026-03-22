class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = {}
        left = 0
        n = len(nums)
        res = 0
        cur_sum = 0

        for right in range(n):
            cur_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if freq[nums[right]] > 1:
                while freq[nums[left]] == 1 and left < right:
                    cur_sum -= nums[left]
                    del freq[nums[left]]
                    left += 1
                cur_sum -= nums[left]
                freq[nums[left]] -= 1
                left += 1

            res = max(res, cur_sum)
        
        return res