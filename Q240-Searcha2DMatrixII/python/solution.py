class Solution:
    def searchMatrixByBoundry(self, matrix: List[List[int]], target: int,
                              right: int, top: int) -> bool:
        if top >= len(matrix):
            return False

        topRow = matrix[top]
        low = 0
        high = right

        while low < high:
            mid = int((low + high) / 2)

            current = topRow[mid]
            #print(f'low {low} high {high} mid {mid} current {current}')

            if current == target:
                return True

            if current < target:
                low = mid + 1
                continue

            if current > target:
                high = mid
                continue

        if low >= right:
            return self.searchMatrixByBoundry(matrix, target, right, top + 1)

        if high < 0:
            return False

        if low == high:
            #print(f'next right {low - 1 }')
            return self.searchMatrixByBoundry(matrix, target, low, top + 1)

        if high < low:
            #print(f'next right {high}')
            return self.searchMatrixByBoundry(matrix, target, high + 1,
                                              top + 1)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchMatrixByBoundry(matrix, target, len(matrix[0]), 0)
