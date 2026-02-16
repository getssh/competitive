class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []

        for el in nums:
            res.append(nums[el])
        
        return res