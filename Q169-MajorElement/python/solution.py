class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        candidate = nums[1]
        counter = 1
        for num in nums[1:]:
            if counter == 0:
                counter = 1
                candidate = num
                continue

            if num == candidate:
                counter = counter + 1
            else:
                counter = counter - 1

        return -1 if counter == 0 else candidate
