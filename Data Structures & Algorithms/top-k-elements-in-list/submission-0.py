class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict()

        for num in nums:
            if num in counts.keys():
                counts[num] += 1
            else:
                counts[num] = 1
        
        sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        res = []
        k_count = 1
        for key in sorted_dict:
            if k_count <= k:
                res.append(key)
                k_count += 1
        return res

