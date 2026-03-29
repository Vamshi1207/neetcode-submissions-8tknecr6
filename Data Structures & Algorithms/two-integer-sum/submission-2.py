class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []

        for i in range(len(nums)):
            remaining = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == remaining:
                    indexes.append(i)
                    indexes.append(j)
                    return indexes