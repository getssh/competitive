class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        start = 0
        end = 0
        idx = -1

        while left <= right:
            mid = (right + (right - left)) // 2

            if nums[mid] == target:
                idx = mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        if idx == -1:
            return [-1, -1]
        
        print(idx)
        i = idx
        j = idx

        if i == 0:
            i = 0
        else:
            while nums[i-1] == target and i >= 0:
                i -= 1
        
        if j == len(nums) - 1:
            j = idx
        else:
            while nums[j+1] == target and j < len(nums):
                j += 1
        
        if i < 0:
            i = 0
        if j > len(nums) - 1:
            j = len(nums) - 1
        
        return [i, j]
