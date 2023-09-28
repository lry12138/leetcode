class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = defaultdict(int)
        for p in paths:
            cities[p[0]] += 1
            cities[p[1]] += 0
        for c in cities:
            if cities[c] == 0:
                return c
