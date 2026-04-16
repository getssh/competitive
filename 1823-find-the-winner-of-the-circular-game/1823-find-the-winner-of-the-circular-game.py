class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        cnt = 0
        turn = 0
        i = 0
        arr = list(range(1, n + 1))

        while len(arr) > 1:
            i = (i + k - 1) % len(arr)
            arr.pop(i)

        return arr[0]
