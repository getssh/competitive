class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        cout = 2 ** (n - 1)
        mid = cout // 2

        if k <= mid:
            return self.kthGrammar(n - 1, k)
        elif k > mid:
            return 1 -self.kthGrammar(n-1, k - mid)