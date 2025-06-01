class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        '''
        TC: O(n)
        AS: O(1)
        '''
        n = len(nums)
        rp = 1
        result = []
        result.append(rp)

        for i in range(1, n):
            rp = rp * nums[i-1]
            result.append(rp)

        rp = 1
        for i in range(n-2, -1, -1):
            rp = rp * nums[i+1]
            result[i] = rp * result[i]

        return result


nums = [-1,1,0,-3,3]
x = Solution()
print(x.productExceptSelf(nums))
