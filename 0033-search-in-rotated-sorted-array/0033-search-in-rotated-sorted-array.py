class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     mid = (left + right) // 2

        #     if nums[mid] == target:
        #         return mid
            
        #     if nums[mid] <= target and nums[left] <= nums[mid]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # return -1