from typing import List
from heapq import heappop,heappush

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        sortedIntervals = sorted(intervals, key = lambda x:x[0])

        print(sortedIntervals)

        rooms = 1

        heap = [sortedIntervals[0][1]]

        for interval in sortedIntervals[1:]:
            startedTime,endTime = (interval[0],interval[1])

            if startedTime >= heap[0]:
                heappop(heap)
                heappush(heap,endTime)
                continue

            if startedTime < heap[0]:
                rooms = rooms + 1
                heappush(heap,endTime)
                continue


        return rooms

if __name__ == "__main__":
    solution = Solution()

    testCases = [
        {
            'input':[[0,30],[5,10],[15,20]],
            'output':2
        },
    ]

    for idx,testCase in enumerate(testCases):
        out = solution.minMeetingRooms(testCase['input'])

        if out!=testCase['output']:
            print(f"test case {idx} failed. expected {testCase['output']} get {out}")
            exit(1)
