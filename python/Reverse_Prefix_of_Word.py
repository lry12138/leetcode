class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        length=len(word)
        if length==1:
            return word
        seen=""
        for i in range(length):
            seen=word[i]+seen
            if word[i] == ch:
                word=seen+word[i+1:length+1]
                break
        return word
