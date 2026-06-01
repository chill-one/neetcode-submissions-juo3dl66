class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
           4.     2.    2.      7.       2.     4.       14
        ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16

       13
       2
       3 // 2 = 1
       3 % 2 = 1

        """
        res = []
        wordList = []
        currentLength = 0

        for idx in range(len(words)):
            word = words[idx]

            if currentLength + len(word) + len(wordList) > maxWidth:
                #How many words are in the list
                leftOverSpace = maxWidth - currentLength
                
                spacePerSpot  = leftOverSpace // max(len(wordList) - 1, 1)
                unEvenSpace  = leftOverSpace % max(len(wordList) - 1, 1)

                for i in range(max(1,len(wordList) - 1)):
                    
                    wordList[i] += " "*spacePerSpot

                    if unEvenSpace:
                        wordList[i] += " "
                        unEvenSpace -= 1
                
                res.append("".join(wordList))
                wordList = []
                currentLength = 0

            wordList.append(word)
            currentLength += len(word)


        last_line = " ".join(wordList)
        leftOver = (maxWidth - len(last_line))
        last_line += " "*leftOver

        res.append(last_line)
                
        return res
