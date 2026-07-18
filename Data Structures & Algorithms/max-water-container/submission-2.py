class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxWater = 0

        i = 0
        j = len(heights) - 1

        while i < j:

            maxHeight = min(heights[i], heights[j])
            width = (j - i)

            maxWater = max(maxWater, maxHeight * width)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return maxWater