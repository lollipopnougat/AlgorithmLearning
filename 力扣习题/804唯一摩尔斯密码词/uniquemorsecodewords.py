class Solution:
    def __init__(self):
        self.m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()
        c = 0
        for i in words:
            tmp = ''.join(map(lambda x: self.m[ord(x) - 97], i))
            if tmp not in s:
                s.add(tmp)
                c += 1
        return c