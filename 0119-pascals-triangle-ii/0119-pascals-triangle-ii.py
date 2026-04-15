class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1], [1, 1]]

        for i in range(2, rowIndex+1):
            temp = []
            lastRow = res[len(res) - 1]

            for j in range(1, len(lastRow)):
                temp.append(lastRow[j] + lastRow[j - 1])
            
            temp.insert(0, 1)
            temp.append(1)
            res.append(temp)
        
        return res[rowIndex]