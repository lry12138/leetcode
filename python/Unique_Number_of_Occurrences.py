class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.Counter(arr)
        occr = defaultdict(int)
        for k,v in dic.items():
            occr[v] += 1
        for k,v in occr.items():
            if v > 1:
                return False
        return True
