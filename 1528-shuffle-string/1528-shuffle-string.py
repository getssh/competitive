class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str_list = list(s)

        for i in range(len(str_list)):
            str_list[indices[i]] = s[i]
        
        return "".join(str_list)
        '''
        codeleet
        lodeceet
        ledecoet
        leeecodt
        leetcode

        '''