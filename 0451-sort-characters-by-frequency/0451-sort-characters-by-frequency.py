class Solution:
    def frequencySort(self, s: str) -> str:
        sort_str = ""
        freq = {}

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]].append(s[i])
            else:
                freq[s[i]] = [s[i]]
        
        str_arr = list(sorted(freq.values(), key=len, reverse=True))

        for st in str_arr:
            sort_str += "".join(st)

        return sort_str