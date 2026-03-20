class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for item in nums[:]:
            if nums.count(item) > 1:
                nums.remove(item)

        return len(nums)        

