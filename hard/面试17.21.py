class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        left = []
        right = []
        max = height[0]
        for i in range(len(height)):
            if height[i] > max:
                max = height[i]
            left.append(max)
        
        max = height[-1]
        for i in range(-1, -1 * len(height) - 1, -1):
            if height[i] > max:
                max = height[i]
            right.append(max)
        right.reverse()

        ans = 0
        for i in range(len(height)):
            h = min(left[i], right[i]) - height[i]
            if h > 0:
                ans += h
        return ans
        
    
