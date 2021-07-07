from typing import List,Set

class Feature:
    cur:str
    longest:str

    def __init__(self,cur:str):
        self.cur = cur
        self.longest:str = cur

    def maxLen(self) -> int:
        return len(self.longest)

    def join(self,other):
        for i in range(other.maxLen()):
            if not self.cur in other.longest[:i+1]:
                self.longest = self.longest + other.longest[i:i+1]
                print(self.cur,self.longest,other.longest[:i+1])
            else:
                break

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        features = [ Feature(x) for x in s]
        maxLen = 1
        lastFeature = features[0]
        for feature in features[1:]:
            feature.join(lastFeature)
            lastFeature = feature
            maxLen = feature.maxLen() if feature.maxLen() > maxLen else maxLen

        return maxLen

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("aaaaaaaa"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
