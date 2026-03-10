class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        left = 0
        
        for right in range(len(s)):
            if s[right] in s[left:right]:
                if len(s[left:right]) > len(longest):
                    longest = s[left:right]

                while s[right] in s[left:right] and left < right:
                    left += 1

        if len(s[left:]) > len(longest):
            longest = s[left:]

        return len(longest)