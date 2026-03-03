class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr_sorted = sorted(score)
        arr_sorted.reverse()
        print(arr_sorted)
        res = []

        for i in range(len(score)):
            if score[i] == arr_sorted[0]:
                res.append("Gold Medal")
            elif score[i] == arr_sorted[1]:
                res.append("Silver Medal")
            elif score[i] == arr_sorted[2]:
                res.append("Bronze Medal")
            else:
                rank = arr_sorted.index(score[i])
                res.append(str(rank+1))
        
        return res