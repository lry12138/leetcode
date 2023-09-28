class Solution:
    def reverseWords(self, s: str) -> str:
        s = ' '.join([x[::-1] for x in s.split()])
        return s
