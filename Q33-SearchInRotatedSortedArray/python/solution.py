from typing import List
import math

class Solution:
    def searchInBoundary(self,nums:List[int],low:int,high:int,target:int) -> int:
        if low == high:
            return -1
        mid = math.floor((low+high)/2)

        if target == nums[mid]:
            return mid

        if mid==low:
            return -1

        if target > nums[mid]:
            if nums[mid] > nums[low]:
                return self.searchInBoundary(nums,mid,high,target)
            else:
                if target >= nums[low]:
                    return self.searchInBoundary(nums,low,mid,target)
                else:
                    return self.searchInBoundary(nums,mid,high,target)

        if target < nums[mid]:
            if nums[mid] < nums[low]:
                return self.searchInBoundary(nums,low,mid,target)
            else:
                if target >= nums[low]:
                    return self.searchInBoundary(nums,low,mid,target)
                else:
                    return self.searchInBoundary(nums,mid,high,target)

    def search(self, nums: List[int], target: int) -> int:
        return self.searchInBoundary(nums,0,len(nums),target)

if __name__ == "__main__":
    print(Solution().search([4,5,6,7,0,1,2],0))
    print(Solution().search([4,5,6,7,0,1,2],3))
    print(Solution().search([1],0))
