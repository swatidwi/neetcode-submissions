class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        
        i,j=0,1

        max_substring_length = 1

        while (j<len(s)):
            substring = s[i:j]
            if s[j] in substring:
                substring_length = len(substring)
                max_substring_length = max(substring_length, max_substring_length)
                while (s[i]!=s[j]):
                    i+=1
                i+=1
                j+=1
            else:
                max_substring_length = max(j-i+1, max_substring_length)
                j+=1

        return max_substring_length

