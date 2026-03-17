class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        cur_vol = 0
        max_vol = 0

        while left <= right:
            width = right - left
            cur_vol = min(height[left], height[right]) * width
            max_vol = max(cur_vol, max_vol)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_vol