class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += f'{len(string)}_{string}'
        return encoded 
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # i points to the start of the string length prefix
            string_len = s[i : i + s[i:].find('_')]
            i += len(string_len) + 1
            # now, i points to the start of the string of interest
            decoded.append(s[i : i + int(string_len)])
            i += int(string_len)

        return decoded

