from typing import List,Dict

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sums:List[int] = []
        hashed:Dict[int,int] = {0:-1}

        cursum = 0
        for idx,val in enumerate(nums):
            cursum = cursum + val
            sums.append(cursum)
            if cursum not in hashed:
                hashed[cursum] = idx 

        maxSub = 0
        cursor = len(sums) - 1
        while cursor >= maxSub and cursor >= 0:
            prefixSum = sums[cursor]
            if (prefixSum - k) in hashed:
                maxSub = maxSub if maxSub > cursor - hashed[prefixSum - k] else cursor - hashed[prefixSum - k]
            cursor = cursor -1

        return maxSub

