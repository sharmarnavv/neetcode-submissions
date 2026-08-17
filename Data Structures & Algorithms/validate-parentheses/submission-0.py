class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {')': '(', '}': '{', ']': '['}
        pstk = []
        for p in s:
            if len(pstk) == 0:
                pstk.append(p)
            else:
                if pmap.get(p) == pstk[-1]:
                    pstk.pop()
        return len(pstk) == 0