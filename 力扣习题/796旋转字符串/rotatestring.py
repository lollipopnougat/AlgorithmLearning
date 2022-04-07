class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ls = len(s)
        lg = len(goal)
        if ls != lg:
            return False
        for i in range(ls):
            j = 0
            if s[i] == goal[j]:
                k = i
                while j < lg and s[k] == goal[j]:
                    k += 1
                    j += 1
                    if k == ls:
                        k = 0
                if j == lg:
                    return True
        return False
        

        
a = "awuvupcrsatnwvxsdbonhyszidtchtisxbiqaekyervvjwfrakopukxbsoorjyioppbqhjmmjzvtjijbubhqhsdtsflvopozqufp"
b = "qufpawuvupcrsatnwvxsdbonhyszidtchtisxbiqaekyervvjwfrakopukxbsoorjyioppbqhjmmjzvtjijbubhqhsdtsflvopoz"

s = Solution()

print(s.rotateString(a,b))
print(s.rotateString('abced','abcde'))