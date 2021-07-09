from typing import List,Set

# slide window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        maxLen = 1
        chars = set()
        chars.add(s[0])
        l = 0
        r = 0
        while l < len(s):
            while r+1 < len(s) and s[r+1] not in chars:
                r = r + 1
                chars.add(s[r])

            maxLen = len(chars) if len(chars) > maxLen else maxLen
            chars.remove(s[l])
            l = l+1

        return maxLen

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("aab"))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("aaaaaaaa"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
