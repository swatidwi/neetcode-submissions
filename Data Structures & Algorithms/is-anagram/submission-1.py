class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        count_map_s = {}
        count_map_t = {}

        for c in s:
            count = count_map_s.get(c, 0)
            count_map_s[c] = count+1

        for c in t:
            count = count_map_t.get(c, 0)
            count_map_t[c] = count+1

        for c1, count1 in count_map_s.items():
            if c1 not in count_map_t:
                return False
            if count_map_t[c1] != count1:
                return False
        return True