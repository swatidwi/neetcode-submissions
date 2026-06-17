class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        "pwwkew"
        if len(s) in [0,1]:
            return len(s)

        max_length = 1
        i=0
        j=1

        while j<len(s):
            if s[j] not in s[i:j]:
                max_length = max(max_length, j-i+1)
                j+=1
            else:
                i+=1 
                # j+=1 - do not do this. move only the i pointer. 
                # moving the j pointer also will make your window contain duplicates because the previous s[j] contains s[i]
        return max_length


        
