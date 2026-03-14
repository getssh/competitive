class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        res = []
        left = 0
        right = len(p) - 1

        for right in range(right, len(s)):
            if sorted(s[left:right+1]) == p:
                res.append(left)
            left += 1
        

        return res