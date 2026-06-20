from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        output = ""
        
        count = len(counter) # why we need count of number of unique letters in t ? otherwise to know if all counts in counter above is 0, 
        # we will have to do - if list(set(counter.values()))[0] == 0 -> instead we can just have a count variable and just check if count == 0
        
        minimum = float("inf")

        l = 0
        r = 0

        while r<len(s):

            while r<len(s) and count!=0:
                if s[r] in counter:
                    counter[s[r]] = counter[s[r]] -1
                    if counter[s[r]] == 0:
                        count = count - 1
                r+=1

            while l<r and count == 0:
                while s[l] not in counter:
                    l+=1
                    continue
                
                # output = s[l:r] # dont do l:r+1 because r is sitting just outside the valid window
                if (r-l) < minimum:
                    minimum = r-l
                    output = s[l:r]

                counter[s[l]] = counter[s[l]] + 1
                if counter[s[l]]>0:
                    count += 1

                # output = s[l:r] # dont do l:r+1 because r is sitting just outside the valid window
                # if (r-l) < minimum:
                #     minumum = r-l
                #     output = s[l:r]

                # if s[l] in counter:
                #     counter[s[l]] = counter[s[l]] + 1
                #     if counter[s[l]]>0:
                #         count += 1
                l+=1
        return output


            
        
                    



