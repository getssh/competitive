class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            divided_sum = sum((num + mid - 1) // mid for num in nums)
            
            if divided_sum > threshold:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
