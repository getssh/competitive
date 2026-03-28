class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()

        i = 0
        j = 0

        while i < len(trainers) and j < len(players):
            if trainers[i] >= players[j]:
                j += 1
                i += 1
            else:
                i += 1
        
        return j