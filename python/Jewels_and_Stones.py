from collections import defaultdict, Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        type_of_stones = collections.Counter(stones)
        jewel_type = set(jewels)
        number = 0
        for i in jewel_type:
            number += type_of_stones[i]
        return number
