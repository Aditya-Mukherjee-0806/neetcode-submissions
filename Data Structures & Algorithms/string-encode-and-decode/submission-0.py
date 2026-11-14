class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = 0
            while s[i + j] != '#':
                j += 1
            l = int(s[i: i + j])
            decoded_strs.append(s[i + j + 1: i + j + l + 1])
            i += l + j + 1
        return decoded_strs