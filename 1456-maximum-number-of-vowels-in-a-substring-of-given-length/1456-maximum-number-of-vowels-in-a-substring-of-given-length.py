class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        max_vowel = 0
        cur_count = 0
        vowels = set("aeiou")

        for i in range(k):
            if s[i] in vowels:
                cur_count += 1
        max_vowel = cur_count

        for right in range(k, len(s)):
            if s[right] in vowels:
                cur_count += 1
            if s[left] in vowels:
                cur_count -= 1
            max_vowel = max(cur_count, max_vowel)

            left += 1
        
        return max_vowel