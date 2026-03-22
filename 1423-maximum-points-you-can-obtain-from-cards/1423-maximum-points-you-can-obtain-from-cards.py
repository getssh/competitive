class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        cur_sum = 0
        res = 0
        left = 0
        win_size = n - k

        for i in range(win_size):
            cur_sum += cardPoints[i]

        res = total - cur_sum

        for right in range(win_size, n):
            cur_sum += cardPoints[right]
            cur_sum -= cardPoints[left]

            res = max(res, total - cur_sum)
            left += 1

        return res