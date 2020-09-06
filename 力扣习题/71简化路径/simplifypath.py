class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        li = path.split('/')
        for i in li:
            if i == '..':
                if res:
                    res.pop()
            elif i == '' or i == '.':
                continue
            else:
                res.append(i)
        return '/' + '/'.join(res)
            

