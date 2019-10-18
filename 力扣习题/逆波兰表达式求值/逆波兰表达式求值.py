class Solution:
    def evalRPN(self, tokens: list) -> int:
        stack = []
        for i in tokens:
            if i in {'+','-','*','/'}:
                num2 = stack.pop()
                num1 = stack.pop()
                res = None
                if i == '+':
                    res = num1 + num2
                elif i == '-':
                    res = num1 - num2
                elif i == '*':
                    res = num1 * num2
                elif i == '/':
                    res = int(num1 / num2)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack.pop()

s = Solution()
res = s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])

print(res)



class Solution2:
    def evalRPN(self, tokens: list) -> int:
        ops = {
            '+':lambda x,y: x + y,
            '-':lambda x,y: x - y,
            '*':lambda x,y: x * y,
            '/':lambda x,y: int(x/y),
        }
        def get_2num(stack):
            r = stack.pop()
            l = stack.pop()
            return l,r
        stack = []
        for t in tokens:
            if t in ops:
                n = ops[t](*get_2num(stack))
                stack.append(n)
            else:
                n = int(t)
                stack.append(n)
        return stack[-1]