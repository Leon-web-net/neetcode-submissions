class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_check = set()

        for i in nums:
            if i in dupe_check:
                return True
            
            dupe_check.add(i)
        
        return False