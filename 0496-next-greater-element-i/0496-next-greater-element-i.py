class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            val = -1

            for j in range(idx + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    val = nums2[j]
                    break

            res.append(val)
        
        return res