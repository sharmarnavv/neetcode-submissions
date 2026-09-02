class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
            
        l, r = 0, len(s) - 1
        st = s.lower()
        
        while l < r:
            if not st[l].isalnum():
                l += 1
                continue
            if not st[r].isalnum():
                r -= 1
                continue
                
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
            
        return True