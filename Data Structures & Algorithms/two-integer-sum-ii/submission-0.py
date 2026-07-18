class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []
        for i in range(len(numbers)):
            remaining = target - numbers[i]
            for j in range(i + 1, len(numbers)):
                if numbers[j] == remaining:
                    res.extend([i+1, j+1])
        return res