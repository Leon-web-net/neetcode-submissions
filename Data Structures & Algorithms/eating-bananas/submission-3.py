class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        lo,hi = 1,max(piles)
        
        while lo<hi:

            mid = (hi-lo)//2 + lo
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)

                if total>h:
                    break
            
            if total>h:
                lo = mid+1
            else:
                hi = mid

        return hi     
                    

        
