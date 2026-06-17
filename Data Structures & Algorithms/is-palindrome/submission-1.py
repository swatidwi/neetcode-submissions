class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        i,j=0,len(s)-1

        while i<j:
            while(i<j and not s[i].isalnum()):
                i+=1
                continue
            while(j>i and not s[j].isalnum()):
                j-=1
                continue
            if (i<j and s[i].lower() == s[j].lower()):
                i+=1
                j-=1
                continue
            else:
                break
        print("i: " + str(i))
        print("j: " + str(j))
        if i==j or i>j:
            return True
        return False
