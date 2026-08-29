class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for idx in range(n-2):
            if idx>0 and nums[idx] == nums[idx-1]:
                continue
            
            if nums[idx] > 0:
                break
            
            target = -nums[idx]
            i,j = idx+1, n-1

            while i<j:
                curr_sum = nums[i] + nums[j]
                if curr_sum == target:
                    res.append([nums[idx], nums[i], nums[j]])
                    i+=1
                    j-=1
                
                    while i<j and nums[i] == nums[i-1]:
                        i+=1
                    while i<j and nums[j] == nums[j+1]:
                        j-=1
                
                elif curr_sum < target:
                    i+=1
                else:
                    j-=1
        
        return res
                