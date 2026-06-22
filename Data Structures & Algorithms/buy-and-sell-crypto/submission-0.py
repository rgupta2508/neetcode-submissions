class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=100000
        res=0
        for i in prices:
            min1=min(min1,i)
            if (i-min1)>res:
                res=i-min1
        return res
        