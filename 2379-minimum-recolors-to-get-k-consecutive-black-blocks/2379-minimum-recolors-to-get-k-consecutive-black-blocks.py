class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        freq = {}
        white_count = float("inf")
        left = 0

        for i in range(k):
            freq[blocks[i]] = freq.get(blocks[i], 0) + 1

        if "W" in freq:
            res = min(white_count, freq["W"])
        else:
            res = 0
        
        for right in range(k, len(blocks)):
            freq[blocks[right]] = freq.get(blocks[right], 0) + 1

            freq[blocks[left]] -= 1
            if "W" in freq:
                white_count = freq["W"]

            if freq[blocks[left]] == 0:
                del freq[blocks[left]]
            
            res = min(white_count, res)

            left += 1
        
        return res