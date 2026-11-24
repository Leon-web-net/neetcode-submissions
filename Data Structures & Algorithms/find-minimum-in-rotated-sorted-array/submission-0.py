class Solution:
    def findMin(self, nums: List[int]) -> int:


        l,r = 0, len(nums)-1

        while l<r:
            
            idx = (r-l)//2 +l
            val = nums[idx]
            
            # l_bool,r_bool = val>l, val>r


            if val<nums[r]:
                r = idx
            else:
                l = idx+1

            # match [l_bool,r_bool]:

            #     case [True,True]:
            #         l = idx+1
            #     case [False, False]:
            #         r = idx
            #     case [True, False]:
            #         r = idx
            #     case [False,True]:
            #         # not possible
            #         break
            
        
        # print(f"l: {l} || r: {r}")
        return nums[r]