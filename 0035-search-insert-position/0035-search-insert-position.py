class Solution(object):
    def searchInsert(self, nums, Target):
        """
        :type nums: List[int]
        :type Target: int
        :rtype: int
        """
        for i in range ( len(nums)):
            if Target==nums[i]:
                return i
            if Target < nums[i] and Target > nums[i-1]:
                return i
            if Target > max(nums):
                return len(nums)
            if Target < min(nums):
                return 0


        