from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero = set()
        one = set()
        more = set()

        for a, b in matches:
            if (a not in one) and (a not in more):
                zero.add(a)

            if b in zero:
                zero.remove(b)
                one.add(b)
            elif b in one:
                one.remove(b)
                more.add(b)
            elif b in more:
                continue
            else:
                one.add(b)
        return sorted(list(zero)), sorted(list(one))
