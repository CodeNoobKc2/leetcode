from typing import List,Tuple

class Solution:
    cur: List[int]
    last: int

    def walk(self) -> tuple[List[int],bool]:
        cur = self.cur.copy()

        i:int = 0
        for i in reversed(range(len(cur))):
            if i == 0:
                continue

            if cur[i] > cur[i-1]:
                j = self.last
                while cur[j] < cur[i-1]:
                    j = j -1

                self.cur[i-1]=cur[j]
                self.cur[j]=cur[i-1]
                self.cur[i:] = reversed(self.cur[i:])
                #print(self.cur)
                break

        return cur,i == 0

    def permute(self, nums: List[int]) -> List[List[int]]:
        ret: List[List[int]] = []
        self.cur = sorted(nums)
        self.last = len(nums) - 1

        while True:
            permutation,exhausted = self.walk()
            ret.append(permutation)
            if exhausted:
                return ret
