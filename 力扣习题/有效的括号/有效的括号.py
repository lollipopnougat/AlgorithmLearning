class Solution:
    def isValid(self, s: str) -> bool:
        ma = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if len(stack) != 0 and i in {')', ']', '}'} and ma[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if len(stack) != 0:
            return False
        else:
            return True