class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        ans = []

        while top <= bottom and left <= right:

            # Top row
            for j in range(left, right + 1):
                ans.append(matrix[top][j])

            top += 1

            # Right column
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])

            right -= 1

            # Bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])

                bottom -= 1

            # Left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])

                left += 1

        return ans
