class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]

        for i in range(2, numRows):
            temp = []
            lastRow = res[len(res) - 1]

            for j in range(1, len(lastRow)):
                temp.append(lastRow[j] + lastRow[j - 1])
            
            temp.insert(0, 1)
            temp.append(1)
            res.append(temp)
        
        return res
        