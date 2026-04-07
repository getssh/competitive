class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.q = []
        self.count = 0
    def consec(self, num: int) -> bool:
        self.q.append(num)

        if self.value != num:
            if self.q:
                self.q.pop(0)
                self.count = 0
        else:
            self.count += 1

        if self.count >= self.k:
            return True
        else:
            return False
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)