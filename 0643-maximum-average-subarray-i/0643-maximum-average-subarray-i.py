class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add next element
            window_sum -= nums[i - k]  # remove element leaving window
            max_sum = max(max_sum, window_sum)
        
        # Return maximum average
        return max_sum / float(k)