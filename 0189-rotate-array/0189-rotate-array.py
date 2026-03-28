class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < 1:
            return nums
        if k > len(nums):
            k = k % len(nums)
        
        arr = nums[-k:] + nums[0:len(nums)-k]

        for i in range(len(nums)):
            nums[i] = arr[i]