class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        lucky = -1
        for k,v in c.items():
            if v == k:
                if lucky < k:
                    lucky = k
        return lucky
