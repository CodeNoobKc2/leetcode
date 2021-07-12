from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()

        h = 0
        for idx,num in enumerate(citations):
            if num >= idx+1:
                h = idx + 1
            else:
                break
        return h

if __name__ == "__main__":
    print(Solution().hIndex([3,0,6,1,5]))
    print(Solution().hIndex([100]))
    print(Solution().hIndex([11,15]))
    print(Solution().hIndex([1,1,3]))
