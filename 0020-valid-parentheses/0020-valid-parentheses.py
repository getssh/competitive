class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if stack and brackets.get(char) == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0
        