class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Track the absolute maximum found so far
        max_sum = nums[0]
        # Track the sum of the current subarray
        current_sum = 0
        
        for num in nums:
            # If current_sum is negative, reset it to 0
            if current_sum < 0:
                current_sum = 0
                
            current_sum += num
            max_sum = max(max_sum, current_sum)
            
        return max_sum
