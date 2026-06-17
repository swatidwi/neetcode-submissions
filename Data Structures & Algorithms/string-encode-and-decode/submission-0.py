class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            length_of_string = len(string)
            result += str(length_of_string)+"#"+string
        return result


    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_of_string = int(s[i:j])
            i = j+1
            j = i+length_of_string
            result.append(s[i:j])
            i = j

        return result
            


            
