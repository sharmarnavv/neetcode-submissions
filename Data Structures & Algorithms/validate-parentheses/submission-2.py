class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {')': '(', '}': '{', ']': '['}
        pstk = []
        
        for p in s:
            if p in pmap:
                if pstk and pstk[-1] == pmap.get(p):
                    pstk.pop()
                else:
                    return False
            else:
                pstk.append(p)
        return len(pstk) == 0