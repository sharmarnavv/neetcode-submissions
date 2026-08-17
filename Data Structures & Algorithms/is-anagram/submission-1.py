class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charmap = {}
        if len(s) != len(t):
            return False
            
        for char in s:
            charmap[char] = charmap.get(char, 0) + 1
        
        for char in t: 
            charmap[char] = charmap.get(char, 0) - 1
            if charmap[char] == -1:
                return False
        return True