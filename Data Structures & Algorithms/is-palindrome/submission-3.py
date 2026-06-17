class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = ""
        for char in s:
            if char.isalnum():
                alnum_s = alnum_s + char

        i=0
        j=len(alnum_s)-1
        while i<j:
            if alnum_s[i].lower() == alnum_s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
