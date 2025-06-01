class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        rp = 1
        result = 0
        result[0] = 1

        for i in range(1, n):
            rp = rp * nums[i-1]
            result[i] = rp

        rp = 1
        for i in range(n-2, 0):
            rp = rp * nums[i+1]
            result[i] = rp * result[i]

        return result
