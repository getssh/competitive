class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        left = 0
        res = 0
        vowels = set("aeiou")

        for left in range(len(word)):
            if word[left] not in vowels:
                continue
            freq = {}

            for right in range(left, len(word)):
                if word[right] not in vowels:
                    break
                if word[right] in freq:
                    freq[word[right]] += 1
                else:
                    freq[word[right]] = 1
                
                if len(freq) == 5:
                    res += 1
        
        return res