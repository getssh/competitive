class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        3 3 4 5
        1 2 2 3
        '''
        people.sort()
        res = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            res += 1
        
        return res