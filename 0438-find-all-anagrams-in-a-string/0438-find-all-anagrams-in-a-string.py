class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        checker = {}
        window = {}
        left = 0
        m = len(p)
        n = len(s)
        res = []

        for i in range(m):
            checker[p[i]] = checker.get(p[i], 0) + 1
            window[s[i]] = window.get(s[i], 0) + 1

        if checker == window:
            res.append(0)

        for right in range(m, n):
            window[s[right]] = window.get(s[right], 0) + 1

            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]
            
            if window == checker:
                res.append(right - m + 1)

            left += 1
        
        return res


        # p = sorted(p)
        # res = []
        # left = 0
        # right = len(p) - 1

        # for right in range(right, len(s)):
        #     if sorted(s[left:right+1]) == p:
        #         res.append(left)
        #     left += 1
        

        # return res