class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += f"{len(string)}#{string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        strs = []
        while i < n:
            str_len = ""
            while s[i] != "#":
                str_len += s[i]
                i += 1
            i += 1
            print(str_len)
            str_len = int(str_len)
            strs.append(s[i : i+str_len])
            i += str_len
        return strs