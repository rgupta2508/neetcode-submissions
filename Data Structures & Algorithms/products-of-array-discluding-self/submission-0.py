class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        temp=1
        for i in range(n):
            ans[i]=temp
            temp=temp*nums[i]
        temp=1
        for j in range(n-1,-1,-1) :
            ans[j]=ans[j]*temp
            temp=temp*nums[j]
        return ans
        