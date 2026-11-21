class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # two loops one for bin search of rows, one for bin search of cols in row

        low, hi = 0, len(matrix)

        while low<hi:
            
            mid = low + math.floor((hi-low)/2)

            if target<matrix[mid][0]:
                hi = mid
            elif target>matrix[mid][-1]:
                low = mid+1
            
            else:

                low_c, hi_c = 0, len(matrix[mid])

                while low_c<hi_c:
                    mid_c = low_c + math.floor((hi_c - low_c)/2)
                    cur_val = matrix[mid][mid_c]
                    if cur_val == target:
                        return True 
                    
                    if cur_val>target:
                        hi_c = mid_c
                    else:
                        low_c = mid_c+1
                
                return False
        
        return False

            
