class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        TC: O(m*n)
        AS:
        """

        m = len(matrix) #rows
        n = len(matrix[0]) #columns

        left = 0
        right = n-1
        top = 0
        bottom = m-1

        # To store output
        result = []


        while left <= right and top <= bottom:
            
            ## top row
            for j in range(left, right+1): # no base condition changed here
                result.append(matrix[top][j])
            top += 1

            ## right row
            for i in range(top, bottom+1): # base condition will be rechecked here for top-bottom as top was increased
                result.append(matrix[i][right])
            right -= 1

            ## bottom row
            if top <= bottom:  # base condition needs to be checked here as bottom is used in the matrix append step
                for j in range(right, left-1, -1):
                    result.append(matrix[bottom][j])
                bottom -=1

            ## left row
            if left <= right: # base condition needs to be checked here as left is used in the matrix append step
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
            



        