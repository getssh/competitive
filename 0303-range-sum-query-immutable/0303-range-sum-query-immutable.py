class NumArray:

    def __init__(self, nums: List[int]):
        cur_sum = 0
        self.res = [cur_sum]
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            self.res.append(cur_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.res[right + 1] - self.res[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)