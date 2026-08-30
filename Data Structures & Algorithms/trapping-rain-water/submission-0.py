class Solution:
    def trap(self, height: List[int]) -> int:
        
        peak_idx = 0
        peak_val = 0

        for i in range(len(height)):
            
            if height[i] >= peak_val:
                peak_idx = i
                peak_val = height[i]
        
        total_area = 0
        lh = 0
        for j in range(peak_idx):

            if height[j]>=lh:
                lh = height[j]
            
            else:
                total_area += lh - height[j]
        
        rh = 0
        for k in range(len(height)-1,peak_idx,-1):
            if height[k]>rh:
                rh = height[k]
            
            else:
                total_area += rh - height[k]
        
        return total_area


