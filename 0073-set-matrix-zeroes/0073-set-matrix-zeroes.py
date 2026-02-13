class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def make_zero(row, col):
            for i in range(0, len(matrix[row])):
                matrix[row][i] = 0
            
            for i in range(0, len(matrix)):
                matrix[i][col] = 0
        
        zeros = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    zeros.append([i, j])
        
        for el in zeros:
            make_zero(el[0], el[1])

