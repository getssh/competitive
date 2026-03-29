class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)

        left = 1
        res = 0
        at_most = 0

        for right in range(1, len(s)):
            if s[right] == s[right-1]:
                at_most += 1
            
            while at_most > 1:
                if s[left] == s[left - 1]:
                    at_most -= 1
                left += 1
            
            res = max(res, right - left + 2)
        
        return res