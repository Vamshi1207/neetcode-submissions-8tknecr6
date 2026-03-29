class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set ()
        for num in nums:
            dups.add(num)

        return False if len(dups) == len(nums) else True