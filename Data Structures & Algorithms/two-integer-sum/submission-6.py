class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i in range(len(nums)):
            for j in range (i + 1, len(nums)):
                currSum = nums[i] + nums[j]
                if currSum == target:
                    res.extend([i, j])
        return res