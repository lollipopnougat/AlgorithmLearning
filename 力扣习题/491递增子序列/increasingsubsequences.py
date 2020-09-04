class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(0,nums,[])
        return self.res 

    def dfs(self,start,nums,track):
        dic = {}
        if len(track)>=2:
            self.res.append(track[:])
        for i in range(start,len(nums)):
            if nums[i] in dic.keys():
                continue
            if track and nums[i]<track[-1]:
                continue
            dic[nums[i]] =1 
            track.append(nums[i])
            self.dfs(i+1,nums,track)
            track.pop()