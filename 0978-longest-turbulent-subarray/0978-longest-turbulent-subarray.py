class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        
        res = 1
        left = 0
        prev_sign = ""
        
        for right in range(1, n):
            if arr[right-1] > arr[right]:
                cur_sign = ">"
            elif arr[right-1] < arr[right]:
                cur_sign = "<"
            else:
                cur_sign = "="

            if cur_sign == "=":
                left = right

            elif cur_sign == prev_sign:
                left = right - 1

            res = max(res, right - left + 1)
            prev_sign = cur_sign
            
        return res
        