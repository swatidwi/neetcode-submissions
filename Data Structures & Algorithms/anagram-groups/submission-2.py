class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_map:
                l = anagram_map[sorted_word]
                l.append(word)
                anagram_map[sorted_word] = l
            else:
                anagram_map[sorted_word] = [word]

        return list(anagram_map.values())