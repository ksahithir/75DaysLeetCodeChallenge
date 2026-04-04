class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for j in range ( len(nums)):
            if target==nums[j]:
                return j
            if target < nums[j] and target > nums[j-1]:
                return j
            if target > max(nums):
                return len(nums)
            if target < min(nums):
                return 0
        