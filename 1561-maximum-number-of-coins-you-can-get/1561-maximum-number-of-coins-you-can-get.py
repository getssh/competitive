class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        '''
        1 2 2 4 7 8 = 7 2 = 9
        1, 2, 3, 4, 5, 6, 7, 8, 9 = 8 6 4 = 18
        '''
        piles.sort()
        res = 0
        n = len(piles)
        start = n // 3

        if n <= 3:
            return piles[1]

        while start < n:
            res += piles[start]
            start += 2
        
        return res
