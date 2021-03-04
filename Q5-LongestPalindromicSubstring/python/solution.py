from typing import Dict,List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest = (0,1)
        offsetToLens:Dict[str,List[int]] = {0:[0,1]}

        for preidx,char in enumerate(s[1:]):
            offsetToLens[preidx+1] = [0,1]
            lens = offsetToLens[preidx]
            for preLen in lens:
                symmetry = preidx - preLen
                if symmetry < 0:
                    continue
                if s[symmetry] == char:
                    candidateLen =  preLen + 2
                    longest = longest if longest[1] - longest[0] >= candidateLen else (symmetry,preidx+2)
                    offsetToLens[preidx+1].append(candidateLen)

        return s[longest[0]:longest[1]]
