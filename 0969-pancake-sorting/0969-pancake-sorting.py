class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        get largest num and flip (put it at index 0)
        put largest back to it's position (put it at index len - 1)
        get second largest and flip (len - prev flips)
        repeat
        (if largest laredy at index 0, do just 1 flip)
        if largest already at len-1 index, no flip go to the next

        3, 2, 1, 4 
        4, 1, 2, 3 k = 4
        3, 2, 1, 4 k = 3
        1, 2, 3, 4 
        res = [4, 3]
        '''
        res = []

        def flip(k, arr):
            start = 0
            end = k - 1
            while start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        size = len(arr)

        for i in range(size, 1, -1):
            max_index = 0

            for j in range(1, i):
                if arr[j] > arr[max_index]:
                    max_index = j

            if max_index != i - 1:
                if max_index != 0:
                    flip(max_index + 1, arr)
                    res.append(max_index + 1)

                flip(i, arr)
                res.append(i)

        return res

