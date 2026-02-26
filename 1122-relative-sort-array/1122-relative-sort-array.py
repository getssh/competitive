class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        rem = []

        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    res.append(arr1[j])
        
        for el in arr1:
            if el not in arr2:
                rem.append(el)
        
        rem.sort()
        ans = res + rem

        return ans