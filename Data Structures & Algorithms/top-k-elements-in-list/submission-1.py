class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        
        for num in nums:
            count[num] = count.get(num,0)+1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []

        for arr in range(len(bucket)-1,0,-1):
            
            # for tie break we can sort each bucket before appending
            # for num in sorted(bucket[arr], reverse=True):

            for num in bucket[arr]: 
                result.append(num)

                if len(result) == k:
                    return result
        
        return nums