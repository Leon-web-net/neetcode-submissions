class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers)-1

        while i<j:

            int_sum = numbers[i] +numbers[j]

            if int_sum == target:
                return [i+1,j+1]

            if int_sum> target:
                j-=1
            
            if int_sum<target:
                i+=1