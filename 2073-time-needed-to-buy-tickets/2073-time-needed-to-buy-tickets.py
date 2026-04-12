class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec = 0
        idx = 0
        n = len(tickets)

        while True:
            if tickets[idx] >= 1:
                tickets[idx] -= 1
                sec += 1
            
            if idx == k and tickets[idx] == 0:
                return sec
            
            idx = (idx + 1) % n