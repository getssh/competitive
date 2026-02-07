class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1
            if freq[el] > len(nums)//2:
                return el
