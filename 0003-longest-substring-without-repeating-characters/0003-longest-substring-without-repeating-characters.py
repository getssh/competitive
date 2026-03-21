class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_len = 0
        left = 0
        freq = {}

        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
                while freq[s[right]] > 1:
                    freq[s[left]] -= 1
                    left += 1
            else:
                freq[s[right]] = 1
            
            cur_len = right - left + 1
            max_len = max(cur_len, max_len)
        

        return max_len