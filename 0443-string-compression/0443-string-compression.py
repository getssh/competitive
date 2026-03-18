class Solution:
    def compress(self, chars: List[str]) -> int:
        group_num = 1
        left = 0

        if len(chars) == 1:
            return 1

        for right in range(1, len(chars)+1):
            if right < len(chars) and chars[right] == chars[right - 1]:
                group_num += 1
            else:
                if group_num == 1:
                    chars[left] = chars[right - 1]
                    left += 1
                    group_num = 1
                elif group_num > 1 and group_num < 10:
                    chars[left] = chars[right-1]
                    chars[left+1] = str(group_num)
                    left += 2
                    group_num = 1
                elif group_num >= 10 and group_num < 100:
                    s = str(group_num)
                    chars[left] = chars[right-1]
                    chars[left+1] = s[0]
                    chars[left+2] = s[1]
                    left += 3
                    group_num = 1
                elif group_num >= 100 and group_num < 1000:
                    s = str(group_num)
                    chars[left] = chars[right-1]
                    chars[left+1] = s[0]
                    chars[left+2] = s[1]
                    chars[left+3] = s[2]
                    left += 4
                    group_num = 1
                elif group_num >= 1000:
                    s = str(group_num)
                    chars[left] = chars[right-1]
                    chars[left+1] = s[0]
                    chars[left+2] = s[1]
                    chars[left+3] = s[2]
                    chars[left+4] = s[3]
                    left += 5
                    group_num = 1

        return left