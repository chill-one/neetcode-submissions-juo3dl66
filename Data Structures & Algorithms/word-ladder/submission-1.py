import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)
        count = 1
        q = deque([(beginWord, 1)])

        while q:
            curr, count = q.popleft()
            if curr == endWord:
                return count
            
            for i in range(len(curr)):
                word = list(curr)
                for char in string.ascii_lowercase:
                    word[i] = char
                    currWord = "".join(word)
                    if currWord in words:
                        q.append((currWord, count+1))
                        words.remove(currWord)


        return 0

                    
            
            

        return 0


        


        




