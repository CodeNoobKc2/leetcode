class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0 :
            return 0

        low = 0
        high = len(height) - 1
        maxArea:int = 0

        while low <= high:
            potential = (high - low ) *  min(height[high],height[low])
            maxArea = max(potential,maxArea)

            if height[low] < height[high]:
                low = low + 1
            else:
                high = high -1

        return maxArea
