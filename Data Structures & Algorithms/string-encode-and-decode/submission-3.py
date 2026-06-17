class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lengths = []
        encoded_word = ""
        for word in strs:
            l = len(word)
            lengths.append(str(l))
            encoded_word = encoded_word + word

        encoded_lengths = ",".join(lengths)
        encoded_word = encoded_lengths + "#" + encoded_word
        return encoded_word


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strings_hash_split = s.split("#")
        encoded_lengths = strings_hash_split[0]
        encoded_word = s[len(encoded_lengths)+1:]
        lengths = encoded_lengths.split(",")
        lengths = [int(l) for l in lengths]

        result = []
        for length in lengths:
            word = encoded_word[:length]
            result.append(word)
            encoded_word = encoded_word[length:]

        return result


