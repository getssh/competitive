class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = {}
        freq_s2 = {}
        left = 0
        n = len(s2)
        m = len(s1)

        if m > n:
            return False
        
        for i in range(m):
            freq_s1[s1[i]] = freq_s1.get(s1[i], 0) + 1
            freq_s2[s2[i]] = freq_s2.get(s2[i], 0) + 1
        
        if freq_s1 == freq_s2:
            return True
        
        for right in range(m, n):
            freq_s2[s2[right]] = freq_s2.get(s2[right], 0) + 1
            
            freq_s2[s2[left]] -= 1

            if freq_s2[s2[left]] == 0:
                del freq_s2[s2[left]]
            
            if freq_s1 == freq_s2:
                return True
            
            left += 1
        
        return False