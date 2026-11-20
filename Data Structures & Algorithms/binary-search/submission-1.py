class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        upper = len(nums)-1
        lower = 0
        n = len(nums)//2

        while lower<=upper:

            if nums[n] == target:
                return n
            
            if nums[n]>target:
                upper = n-1
            else:
                lower = n+1
            
            n = (lower+upper)//2
        

        return -1
