class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        res=0
        temp=0
        for i,ch in enumerate(s):
            if ch in seen and seen[ch]>=temp:
                temp=seen[ch]+1
            seen[ch] = i
            res = max(res, i - temp + 1)


        return res


        