class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += f"{len(word)}#{word}"
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])

            words.append(s[j+1:j+1+str_len])
            i = j+1+str_len
        return words

