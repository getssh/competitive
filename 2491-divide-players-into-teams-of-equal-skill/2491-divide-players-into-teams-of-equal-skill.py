class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        '''
        3,2,5,1,3,4
        1 2 3 3 4 5 
        '''
        skill.sort()
        res = 0
        n = len(skill)
        cur_skill = skill[0] + skill[n-1]
        left = 0
        right = n - 1

        while left <= right:
            if skill[left] + skill[right] != cur_skill:
                return -1
            else:
                res += (skill[left] * skill[right])
            left += 1
            right -= 1
        
        return res
