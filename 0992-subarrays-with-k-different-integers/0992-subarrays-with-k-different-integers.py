class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        at_most_k = 0
        at_most_k_1 = 0
        left = 0
        freq_1 = {}
        freq_2 = {}

        for right in range(n):
            freq_1[nums[right]] = freq_1.get(nums[right], 0) + 1

            while len(freq_1) > k and left < right:
                freq_1[nums[left]] -= 1
                if freq_1[nums[left]] == 0:
                    del freq_1[nums[left]]
                left += 1

            at_most_k += right - left + 1

        left = 0

        if k > 1:
            for right in range(n):
                freq_2[nums[right]] = freq_2.get(nums[right], 0) + 1

                while len(freq_2) > k - 1 and left < right:
                    freq_2[nums[left]] -= 1
                    if freq_2[nums[left]] == 0:
                        del freq_2[nums[left]]
                    left += 1

                at_most_k_1 += right - left + 1
        
        
        return at_most_k - at_most_k_1
                