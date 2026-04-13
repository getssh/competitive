class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        que = []

        for c in s:
            freq[c] = freq.get(c, 0) + 1
            que.append(c)
        
        for i in range(len(s)):
            if freq[que[i]] == 1:
                return i
        
        return -1
        