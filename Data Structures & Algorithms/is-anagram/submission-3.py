class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = {}
        t_counter = {}

        for s_char in s:
            if s_counter.get(s_char, 0) == 0:
                s_counter[s_char] = 1
            else:
                s_counter[s_char] += 1
        for t_char in t:
            if s_counter.get(t_char,0) == 0:
                return False
            if t_counter.get(t_char, 0) == 0:
                t_counter[t_char] = 1
            else:
                t_counter[t_char] += 1
        return s_counter == t_counter
