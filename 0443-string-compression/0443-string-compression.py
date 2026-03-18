from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        group_num = 1
        left = 0
        n = len(chars)

        if n <= 1:
            return n

        for right in range(1, n + 1):
            if right < n and chars[right] == chars[right - 1]:
                group_num += 1
            else:
                chars[left] = chars[right - 1]
                left += 1
                
                if group_num > 1:
                    for digit in str(group_num):
                        chars[left] = digit
                        left += 1
                
                group_num = 1

        return left