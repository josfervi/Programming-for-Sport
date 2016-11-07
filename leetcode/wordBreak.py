# may be incorrect

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # Base Case
        try:
            wordDict.index(s)
            return True
        except:
            pass
        
        # Recursive Case
        for i in range(1, len(s)):
            try:
                wordDict.index(s[:i])
                return self.wordBreak(s[i:], wordDict)
            except:
                pass
            
        return False

sol= Solution()
a= sol.wordBreak("leetcode", ["leet", "code"])
print a