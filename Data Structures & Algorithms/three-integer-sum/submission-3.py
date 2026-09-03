class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue    
            target = -(sorted_nums[i])
            j, k = i + 1, len(sorted_nums)-1
            while j <  k:
                if sorted_nums[j] + sorted_nums[k] > target:
                    k -= 1
                elif sorted_nums[j] + sorted_nums[k] < target:
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] == target:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k + 1]:
                        k -= 1
        return res