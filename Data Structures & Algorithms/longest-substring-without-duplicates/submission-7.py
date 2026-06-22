class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        res=0
        left=0
        for right,ch in enumerate(s):
            if ch in seen and seen[ch]>=left:
                left=seen[ch]+1
            seen[ch] = right
            res = max(res, right - left + 1)


        return res


        