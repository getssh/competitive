class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        1 2 3
        4 5 6
        '''

        res = []

        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            res.append(temp)
        return res