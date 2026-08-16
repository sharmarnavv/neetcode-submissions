"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def merge(self, a, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = a[l + i]
        
        for j in range(n2):
            R[j] = a[m + j + 1]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i].start <= R[j].start:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        
        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, a, l, r):
        if l < r:
            m = l + (r-l)//2

            self.merge_sort(a, l, m)
            self.merge_sort(a, m+1, r)
            self.merge(a, l, m, r)

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        self.merge_sort(intervals, 0, n-1)
        for i in range(1, n):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True