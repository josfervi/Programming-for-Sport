def wordLadder(beginWord, endWord, wordList):
    
    def dist(word1, word2):
        return sum(c1 != c2 for c1, c2 in zip(word1, word2))

    ans = 1
    active = {beginWord}
    wordset = set(wordList)
    while active:
        if endWord in active:
            return ans
        active = {y for x in active for y in wordset if dist(x, y) == 1}
        wordset -= active
        ans += 1
    return 0
