class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        [1,0,2,3,0,4,5,0]
        [1,0,0,2,3,0,4,5]        
        [1,0,0,2,3,0,5,4]        
        """
        def shift_el(idx):
            for i in range(len(arr)-1, idx, -1):
                temp = arr[i-1]
                arr[i] = temp
        
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                shift_el(i)
                i += 2
            else:
                i += 1