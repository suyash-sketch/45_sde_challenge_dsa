class Solution:
    def trap(self, height: list[int]):
        n = len(height)

        left, right = 0, n - 1
        
        max_left = 0
        max_right = 0

        total_water = 0

        while left <= right:
            if height[left] <= height[right]:

                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left+=1
            else:

                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                
                right-=1
            
        return total_water