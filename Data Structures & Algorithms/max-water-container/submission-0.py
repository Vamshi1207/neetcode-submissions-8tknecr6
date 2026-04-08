class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCap = 0
        for i in range(len(heights)):
            for j in range(len(heights) - 1, -1, -1):
                minHeight = min(heights[i], heights[j])
                distance = j - i

                tmp = minHeight * distance

                maxCap = max(tmp, maxCap)
        
        return maxCap
