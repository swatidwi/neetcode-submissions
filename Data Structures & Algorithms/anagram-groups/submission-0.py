class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} # map of sorted chars and list of matching anagrams

        for word in strs:
            s_word_list = sorted(word)
            s_word = ''.join(s_word_list)
            if s_word in seen:
                seen[s_word].append(word)
            else:
                seen[s_word] = [word]
        
        return list(seen.values())