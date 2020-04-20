from collections import defaultdict
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.twitter_list = defaultdict(list)
        self.followed_info = defaultdict(list)
        self.no = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.twitter_list[self.no] = (userId, tweetId)
        self.no += 1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        num = 0
        res = []
        for i in range(len(self.twitter_list) - 1, -1, -1):
            if num > 9:
                break
            if self.twitter_list[i][0] == userId or (
                    userId in self.followed_info.keys()
                    and self.twitter_list[i][0] in self.followed_info[userId]):
                res.append(self.twitter_list[i][1])
                num += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followed_info[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followed_info[followerId]:
            self.followed_info[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
tt = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
tt.postTweet(1, 5)
tt.postTweet(2, 3)
tt.postTweet(1, 101)
tt.postTweet(2, 13)
tt.postTweet(2, 10)
tt.postTweet(1, 2)
tt.postTweet(1, 94)
tt.postTweet(2, 505)
tt.postTweet(1, 333)
tt.postTweet(2, 22)
tt.postTweet(1, 11)
tt.postTweet(1, 205)
tt.postTweet(2, 203)
tt.postTweet(1, 201)
tt.postTweet(2, 213)
tt.postTweet(1, 200)
tt.postTweet(2, 202)
tt.postTweet(1, 204)
tt.postTweet(2, 208)
tt.postTweet(2, 233)
tt.postTweet(1, 222)
tt.postTweet(2, 211)
print(tt.getNewsFeed(1))
tt.follow(1, 2)
print(tt.getNewsFeed(1))
tt.unfollow(1, 2)
print(tt.getNewsFeed(1))
