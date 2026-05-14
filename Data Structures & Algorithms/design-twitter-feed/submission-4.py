class Twitter:
    """
    postTweet 
    """

    def __init__(self):
        self.usersFollow = defaultdict(set)
        self.recentTweet = []
        self.tweet = defaultdict(list)
        self.tweetNum = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.tweetNum, tweetId))
        self.tweetNum += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        Group_users = list(self.usersFollow[userId]) + [userId]
        minHeap = []

        for user in Group_users:
            tweets = self.tweet[user]
            for time, tweet in tweets:
                heapq.heappush(minHeap, (time, tweet))
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

        result_tweet = []
        while minHeap:
            time, recent_tweet = heapq.heappop(minHeap)
            result_tweet.append(recent_tweet)


        return result_tweet[::-1]



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.usersFollow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.usersFollow[followerId].discard(followeeId)
        
