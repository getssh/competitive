class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        first = 0
        second = 0
        res = []

        if n1 < 1 or n2 < 1:
            return []

        while first < n1 and second < n2:
            start_interval = max(firstList[first][0], secondList[second][0])
            end_interval = min(firstList[first][1], secondList[second][1])

            if end_interval >= start_interval:
                res.append([start_interval, end_interval])
            
            if firstList[first][1] >= secondList[second][1]:
                second += 1
            else:
                first += 1
        
        return res
