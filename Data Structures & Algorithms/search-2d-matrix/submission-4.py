class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get(mat, x):
            #m = len(mat)
            n = len(mat[0])
            i = x // n
            j = x % n
            return mat[i][j]
        
        def helper(mat, a, b, targ):
            if (a > b):
                return False
            mid = (a+b)//2
            print(mid)
            if mid//len(mat[0]) >= len(mat):
                return False
            if (get(mat, mid) == targ):
                return True
            elif (get(mat, mid) < targ):
                return helper(mat, mid + 1, b, targ)
            else:
                return helper(mat, a, mid - 1, targ)

        return helper(matrix, 0, len(matrix)*len(matrix[0]), target)