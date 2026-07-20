import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        res = []
        for x1, y1 in points:
            distance = math.sqrt(x1**2 + y1**2)
            tmp = [[x1, y1], [distance]]
            res.append(tmp)
        top_k_elements = sorted(res, key=lambda x: x[1][0])[:k]
        return [item[0] for item in top_k_elements]
        
