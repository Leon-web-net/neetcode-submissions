class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets_dict = {'(':')','[':']','{':'}'}
        stack = deque()
        
        for c in s:

            if c in brackets_dict:
                stack.append(brackets_dict[c])
            else:
                if not stack or stack.pop()!= c:
                    return False
        
        return True if not stack else False





