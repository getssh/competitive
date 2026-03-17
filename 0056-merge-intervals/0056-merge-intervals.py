class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        n = len(intervals)

        for i in range(1, n):
            last = res[-1][1]

            if intervals[i][0] <= last:
                start = intervals[i][0]
                res[-1][1] = max(intervals[i][1], last)
            else:
                res.append(intervals[i])

        return res