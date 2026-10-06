class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s or len(t) > len(s):
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c,0) +1

        window = {}
        have, required = 0,len(need)
        best = [-1,-1]
        best_len = float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) +1

            if c in need and window[c] == need[c]:
                have +=1
            
            while have == required:
                if(right - left+1) <best_len:
                    best = [left, right]
                    best_len = right - left+1

                out = s[left]
                window[out]-=1
                if out in need and window[out] <need[out]:
                    have -=1
                
                left +=1
        
        l,r = best
        return s[l:r+1] if best_len != float("inf") else ""