class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        curr = 0
        x = 1
        while curr < len(nums):
            for j in range(len(nums)):
                if j != curr:
                    x *= nums[j]
            res.append(x)
            curr += 1
            x = 1

        return res
                
