class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        recallSet = set()
        for num in nums:
            if num in recallSet:
                return True
            recallSet.add(num)
        return False 