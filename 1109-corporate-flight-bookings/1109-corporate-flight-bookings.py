class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)

        for flight in bookings:
            start = flight[0] - 1
            end = flight[1]

            res[start] += flight[2]
            res[end] -= flight[2]
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        return res[:n]