class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        upper = len(nums)-1
        lower = 0
        n = len(nums)//2

        while lower<=upper:

            mid = (lower+upper)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid+1
            else:
                upper = mid-1
        
        return -1