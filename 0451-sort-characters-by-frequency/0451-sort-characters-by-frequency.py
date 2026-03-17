class Solution:
    def frequencySort(self, s: str) -> str:
        sort_str = ""
        freq = {}

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
        
        # str_arr = list(sorted(freq.values(), key=len, reverse=True))
        sorted_chars = list(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        print(sorted_chars)
        for st in sorted_chars:
            sort_str += st[0] * st[1]

        return sort_str