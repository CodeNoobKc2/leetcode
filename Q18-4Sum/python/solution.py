from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []

        nums.sort()
        ret = []
        print(nums)

        lastTwoSum = nums[len(nums)-1] + nums[len(nums)-2]
        pre0 = nums[0] - 1
        for i,num0 in enumerate(nums[0:len(nums)-3]):
            if num0 == pre0:
                continue
            pre1 = pre0
            pre0 = num0
            print(f'i {i}')
            for j,num1 in enumerate(nums[i+1:len(nums)-2]):
                j = j + i + 1
                if num1 == pre1:
                    continue
                print(f'j {j}')
                pre1 = num1
                if num1 + num0 + lastTwoSum < target:
                    continue
                if num1 + num0 + nums[j+1] + nums[j+2] > target:
                    continue
                left = j+1
                right = len(nums) - 1
                while left<right:
                    print(f'{i} {j} {left} {right}')
                    if num0 + num1 + nums[left] + nums[right] == target:
                        ret.append([num0,num1,nums[left],nums[right]])
                        cur = nums[left]
                        while left < right and  nums[left] == cur:
                            left = left + 1
                        continue
                    if num0 + num1 + nums[left] + nums[right] < target:
                        cur = nums[left]
                        while left < right and  nums[left] == cur:
                            left = left + 1
                        continue
                    if num0 + num1 + nums[left] + nums[right] > target:
                        cur = nums[right]
                        while left < right and nums[right] == cur:
                            right = right -1
                        continue
        return ret

if __name__ == "__main__":
    #print(Solution().fourSum([1,0,-1,0,-2,2],0))
    #print(Solution().fourSum([0,0,0,0],0))
    print(Solution().fourSum([-1,0,1,2,-1,-4],-1))
