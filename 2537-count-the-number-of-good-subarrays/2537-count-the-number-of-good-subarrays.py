class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}
        left = 0
        current_pairs = 0
        ans = 0
        
        for right in range(n):
            num_r = nums[right]
            
            count = freq.get(num_r, 0)
            current_pairs += count
            
            freq[num_r] = count + 1
            
            while current_pairs >= k:
                ans += (n - right)

                num_l = nums[left]
                freq[num_l] -= 1
                
                current_pairs -= freq[num_l]
                left += 1
                
        return ans