class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        '''
        12 12 14 19 19
         2  7 17 19 20
        10  5  3  0  1  
        '''
        res = 0
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        
        return res