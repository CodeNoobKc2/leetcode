from typing import Dict,List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest = s[0]
        palindromes:Dict[str,List[str]] = {0:[s[0],""]}

        for preidx,char in enumerate(s[1:]):
            palindromes[preidx+1] = ["",char]
            pres = palindromes[preidx]
            for pre in pres:
                symmetry = preidx - len(pre)
                if symmetry < 0:
                    continue
                if s[symmetry] == char:
                    candidate = char + pre + char
                    longest = candidate if len(candidate) > len(longest) else longest
                    palindromes[preidx+1].append(candidate)

        return longest
