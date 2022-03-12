class Solution:
    def convertToBase7(self, num: int) -> str:
        st = []
        isLessThanZero = False
        if num < 0:
            isLessThanZero = True
            num = -num
        t = num // 7
        while t > 0:
            st.insert(0, str(num - t * 7))
            num = t
            t = num // 7
        st.insert(0, str(num))
        if isLessThanZero:
            st.insert(0, '-')
        return ''.join(st)

s = Solution()
for i in range(-36, 36):
    print(s.convertToBase7(i))