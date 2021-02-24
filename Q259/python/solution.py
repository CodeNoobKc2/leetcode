from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            return 0

        cnt = 0
        last = len(nums) - 2
        tot = len(nums)
        nums = sorted(nums)

        pre = nums[0] - 1
        idx = 0

        while idx < last:
            left = idx + 1
            right = tot - 1

            while left < right:
                cursum = nums[idx] + nums[left] + nums[right]
                print(f'nums {nums}, cur {idx} ,left {left},right {right}, cursum {cursum}, target {target}')
                if cursum < target:
                    delta = right - left
                    cnt = cnt + delta 
                    print(f'added {delta}')
                    left = left + 1
                    continue

                if cursum >= target:
                    rval = nums[right]
                    while right > left and nums[right] is rval:
                        right = right - 1
                    continue

            idx = idx + 1

        return cnt

if __name__ == "__main__":
    solution = Solution()

    inputs = [
        {'nums':[-2,0,1,3],'target':2},
        {'nums':[3,1,0,-2],'target':4},
        {'nums':[1,1,-2],'target':1},
        {'nums':[1,-2,2,1,0],'target':1},
        {'nums':[2,0,0,2,-2],'target':2},
    ]

    outputs = [
        2,
        3,
        1,
        4,
        5
    ]

    for idx,tinput in enumerate(inputs):
        print(f'test case {0} begin -------')
        computed = solution.threeSumSmaller(tinput['nums'],tinput['target'])
        if computed != outputs[idx]:
            print(f'test case {idx} failed. expected {outputs[idx]} get {computed}')
            exit(1)
        print(f'test case {0} pass -------')
