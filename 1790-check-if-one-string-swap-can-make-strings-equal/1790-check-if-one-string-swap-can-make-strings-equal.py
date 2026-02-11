class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        swap1 = ""
        swap2 = ""

        for i in range(len(s1)):
            if (s1[i] != s2[i]):
                diff += 1
                swap1 += s1[i]
                swap2 += s2[i]
        if diff <= 2:
            if "".join(sorted(swap1)) == "".join(sorted(swap2)):
                return True
            else:
                return False
        else:
            return False