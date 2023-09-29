class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        if numRows == 0:
            return pascal
        
        first = [1]
        pascal.append(first)
        
        for i in range(1,numRows):
            prev = pascal[i-1]
            curr = [1]
            for j in range(1,i):
                curr.append(prev[j-1]+prev[j])

            curr.append(1)
            pascal.append(curr)
        return pascal

        
