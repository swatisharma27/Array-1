class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        '''
        TC: O(m*n)
        AS: O(1)
        '''

        if not mat or not mat[0]:
            return []
        
        m = len(mat) # rows
        n = len(mat[0]) #columns
        result = []
        idx = 0
        i = 0
        j = 0
        direction = True

        while len(result) < m*n:
            result.append(mat[i][j])
            if direction: #Upward Direction --> breach "top" and "right"
                # 1) Top Breach
                if i==0 and j!=n-1:  ## As for one of the corener i==0 and j!=n-1 both if statements are true so j!=n-1
                    direction = False #changes to downwards
                    j += 1
                # 2) Right Breach
                elif j==n-1:
                    direction = False
                    i +=1
                # 3) No Breach
                else:
                    j += 1
                    i -= 1
            else:
                # 1) Left Breach
                if j==0 and i!=m-1: ## As for one of the corener i!=n-1 and j==0 both if statements are true so i!=m-1
                    direction = True #changes to upwards
                    i += 1

                # 2) Right Breach
                elif i==m-1:
                    direction = True
                    j += 1

                # 3) No Breach
                else:
                    j -= 1
                    i += 1
        
        return result