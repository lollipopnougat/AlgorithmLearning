from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        it = iter(letters)
        for i in it:
            if ord(i) > ord(target):
                return i
        return letters[0]