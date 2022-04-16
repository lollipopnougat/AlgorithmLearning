# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.is_list = value == None
        self.list = []
        self.val = value

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return not self.is_list

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.is_list = True
        self.list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.is_list = False
        self.val = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if not self.is_list:
            return self.val
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.is_list:
            return self.is_list
        else:
            return None
    def __str__(self):
        return self.to_str()

    def __repr__(self):
        return self.to_str()

    def to_str(self):
        st = []
        if self.is_list:
            st.append('[')
            for i in self.list:
                if i.is_list:
                    st.extend(i.to_str())
                else:
                    st.append(str(i.getInteger()))
                st.append(',')
            if st[-1] == ',': 
                st.pop()                
            st.append(']')
        else:
            st.append(str(self.getInteger()))
        return ''.join(st)

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        numstr = []
        stack = []
        for i in s:
            if i == '[':
                stack.append(i)
            elif 47 < ord(i) < 58 or i == '-':
                numstr.append(i)
            elif i == ',':
                if numstr:
                    tmp = NestedInteger(int(''.join(numstr)))
                    stack.append(tmp)
                    numstr.clear()
            elif i == ']':
                if numstr:
                    tmp = NestedInteger(int(''.join(numstr)))
                    stack.append(tmp)
                    numstr.clear()
                t = NestedInteger()
                tm = []
                while stack and stack[-1] != '[':
                    tm.insert(0, stack.pop())
                if stack and stack[-1] == '[':
                    stack.pop()
                for i in tm:
                    t.add(i)
                stack.append(t)
        if numstr:
            tmp = NestedInteger(int(''.join(numstr)))
            stack.append(tmp)
            numstr.clear()
        return stack[0]


s = Solution()

# a = s.deserialize('[123,[456,[789]]]')
a = s.deserialize("[123,456,[788,799,833],[[]],10,[]]")
print(a.to_str())