class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window problem
        # what sthe condition when the window is valid ?
        #(r-l+1) - count_of_the max_char <= k then the window is valid
         
        l=0
        r=0
        char_count_map = {}
        max_length = 0

        while r<len(s):
            char_count_map[s[r]] = char_count_map.get(s[r], 0) + 1
            max_char_count_in_window = max(char_count_map.values())
            if ((r-l+1) - max_char_count_in_window) <= k:
                max_length = max(max_length, r-l+1)
                r +=1
            else:
                # window is not valid anymore, we will move l till the window is valid again
                while ((r-l+1) - max_char_count_in_window) > k:
                    char_count_map[s[l]] = char_count_map[s[l]] - 1
                    max_char_count_in_window = max(char_count_map.values())
                    l+=1
                r+=1

        return max_length



