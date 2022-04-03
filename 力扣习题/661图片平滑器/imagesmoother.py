from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        res = [([0] * m) for _ in range(n)]
        if n == m == 1:
            res[0][0] = img[0][0]
        if n > 1 and m > 1:
            res[0][0] = (img[0][0] + img[0][1] + img[1][0] + img[1][1]) // 4
            res[0][m - 1] = (img[0][m - 2] + img[0][m - 1] + img[1][m - 1] + img[1][m - 2]) // 4
            res[n - 1][0] = (img[n - 1][0] + img[n - 1][1] + img[n - 2][0] + img[n - 2][1]) // 4
            res[n - 1][m - 1] = (img[n - 1][m - 1] + img[n - 1][m - 2] + img[n - 2][m - 1] + img[n - 2][m - 2]) // 4
        elif n > 1 and m == 1:
            res[0][0] = (img[0][0] + img[1][0]) // 2
            res[n - 1][0] = (img[n - 1][0] + img[n - 2][0]) // 2
            for i in range(1, n - 1):
                res[i][0] = (img[i - 1][0] + img[i][0] + img[i + 1][0]) // 3
            return res
        elif m > 1 and n == 1:
            res[0][0] = (img[0][0] + img[0][1]) // 2
            res[0][m - 1] = (img[0][m - 1] + img[0][m - 2]) // 2
            for i in range(1, m - 1):
                res[0][i] = (img[0][i - 1] + img[0][i] + img[0][i + 1]) // 3
            return res
        for i in range(1, m - 1):
            su = 0
            su += img[0][i - 1] + img[0][i] + img[0][i + 1] + img[1][i - 1] + img[1][i] + img[1][i + 1]
            res[0][i] = su // 6
            su = 0
            su += img[n - 1][i - 1] + img[n - 1][i] + img[n - 1][i + 1] + img[n - 2][i - 1] + img[n - 2][i] + img[n - 2][i + 1]
            res[n - 1][i] = su // 6
        for i in range(1, n - 1):
            su = 0
            su += img[i - 1][0] + img[i][0] + img[i + 1][0] + img[i - 1][1] + img[i][1] + img[i + 1][1]
            res[i][0] = su // 6
            su = 0
            su += img[i - 1][m - 1] + img[i][m - 1] + img[i + 1][m - 1] + img[i - 1][m - 2] + img[i][m - 2] + img[i + 1][m - 2]
            res[i][m - 1] = su // 6
        for i in range(1, n - 1):
            for j in range(1 , m - 1):
                su = 0
                su += img[i - 1][j - 1] + img[i - 1][j] + img[i - 1][j + 1] + img[i][j - 1] + img[i][j] + img[i][j + 1] + img[i + 1][j - 1] + img[i + 1][j] + img[i + 1][j + 1]
                res[i][j] = su // 9
        return res

s = Solution()
li = [[1,1,1],[1,0,1],[1,1,1]]
l2 = [[100,200,100],[200,50,200],[100,200,100]]
l3 = [[1]]
l4 = [[1, 5]]
l41 = [[1, 5, 1]]
l5 = [[1],[2]]
l51 = [[1], [2], [3]]
print(s.imageSmoother(li))
print(s.imageSmoother(l2))
print(s.imageSmoother(l3))
print(s.imageSmoother(l4))
print(s.imageSmoother(l41))
print(s.imageSmoother(l5))
print(s.imageSmoother(l51))

