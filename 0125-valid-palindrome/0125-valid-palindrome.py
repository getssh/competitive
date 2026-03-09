class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(char):
            return char.isalnum()

        clean = ""

        for i in s:
            if check(i):
                clean += i

        clean = clean.lower()

        return clean == clean[::-1]