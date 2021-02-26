class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ret:List[List[int]] = []

        rightMax = -1

        for interval in intervals:
            if interval[0] > rightMax:
                ret.append(interval)
                rightMax = interval[1]
            else:
                ret[len(ret)-1][1] = interval[1] if interval[1] > ret[len(ret)-1][1] else ret[len(ret)-1][1]
                rightMax = ret[len(ret)-1][1]
        return ret
