class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_val = float('-inf')
        x_vals = []

        for point in points:
            x_vals.append(point[0])
        
        x_vals.sort()

        for i in range(1, len(x_vals)):
            max_val = max(max_val, x_vals[i] - x_vals[i-1])
        
        return max_val