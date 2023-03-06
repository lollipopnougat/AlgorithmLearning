class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split()
        t.reverse()
        return ' '.join(t)