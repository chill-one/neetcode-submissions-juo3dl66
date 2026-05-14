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

        for u in Group_users:
            tweets = self.tweet[u]
            if tweets:
                time, tid = tweets[-1]
                heapq.heappush(minHeap, (-time, tid, u, len(tweets) - 2))

        
        res = []
        while minHeap and len(res) < 10:
            neg_time, tid, uid, idx = heapq.heappop(minHeap)
            res.append(tid)
            if idx >= 0:
                time, tid = self.tweet[uid][idx]
                heapq.heappush(minHeap, (-time, tid, uid, idx-1))

        return res
            

        


        return result_tweet[::-1]



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.usersFollow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.usersFollow[followerId].discard(followeeId)
        
