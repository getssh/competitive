class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        left = 0
        res = 0
        
        if len(fruits) <= 2:
            return len(fruits)
            
        for i in range(2):
            freq[fruits[i]] = freq.get(fruits[i], 0) + 1

        res = len(freq)

        for right in range(2, len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1

            while len(freq) > 2 and left < right:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                
                left += 1
            
            res = max(res, right - left + 1)
        
        return res