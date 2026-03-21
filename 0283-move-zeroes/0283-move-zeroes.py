class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        result=[]
        for i in range(0,len(nums)):
            if nums[i]!=0:
                result.append(nums[i])
        final = result + [0] * (len(nums) - len(result))
        for i in range(len(nums)):
            nums[i] = final[i]
   
            
            
                

               
                
            