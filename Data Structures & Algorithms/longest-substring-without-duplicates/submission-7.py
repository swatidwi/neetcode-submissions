class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        if len(s) in [0,1]:
            return len(s)

        max_length = 1
        l=0
        r=1

        while r<len(s):
            if s[r] not in s[l:r]:
                max_length = max(max_length, r-l+1)
                r+=1
            else:
                while (s[r] in s[l:r]):
                    l+=1 
                
        return max_length


        
