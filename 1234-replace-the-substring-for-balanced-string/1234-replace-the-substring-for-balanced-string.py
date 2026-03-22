class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        
        counts = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for char in s:
            counts[char] += 1
            
        if counts['Q'] <= target and counts['W'] <= target and \
           counts['E'] <= target and counts['R'] <= target:
            return 0
            
        res = n
        left = 0
        
        for right in range(n):
            counts[s[right]] -= 1
            
            while left < n and counts['Q'] <= target and counts['W'] <= target and \
                  counts['E'] <= target and counts['R'] <= target:
                
                res = min(res, right - left + 1)
                
                counts[s[left]] += 1
                left += 1
                
        return res
        