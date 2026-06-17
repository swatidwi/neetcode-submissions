from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        s_char_map = defaultdict(int)
        for c in s:
            s_char_map[c] = s_char_map[c] + 1

        for c in t:
            if c not in s_char_map:
                return False
            if s_char_map[c] <= 0:
                return False
            s_char_map[c] = s_char_map[c] - 1

            if s_char_map[c] == 0:
                s_char_map.pop(c, None)
            
        if s_char_map:
            return False
        return True

