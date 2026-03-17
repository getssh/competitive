class NumArray:

    def __init__(self, nums: List[int]):
        cur_sum = nums[0]
        self.res = [cur_sum]
        
        for i in range(1, len(nums)):
            cur_sum += nums[i]
            self.res.append(cur_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.res[right]
        return self.res[right] - self.res[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)