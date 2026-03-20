class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        -4 -1 -1 0 1 2
        [-100,-70,-60,110,120,130,160]
        '''
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1


                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return res
