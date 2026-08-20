from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = defaultdict(int)
        t_counter = defaultdict(int)

        for char in s:
            s_counter[char] += 1
        for char in t:
            if s_counter.get(char, 0) == 0:
                return False
            s_counter[char] -= 1
        return True
