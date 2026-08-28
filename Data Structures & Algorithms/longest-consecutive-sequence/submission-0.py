class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0

        for num in num_set:
            if num -1 not in num_set:
                curr = num
                curr_seq_length = 1

                while curr+1 in num_set:
                    curr+=1
                    curr_seq_length+=1
                
                longest_seq = max(longest_seq, curr_seq_length)
        
        return longest_seq