class Solution:
    def minOperations(self, logs: List[str]) -> int:
        '''
        d1 d2 d31
        '''
        stack = []

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        
        return len(stack)
