class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for s_char, t_char in zip(s,t):
            counter[ord(s_char) - ord('a')] += 1
            counter[ord(t_char) - ord('a')] -= 1
        
        for num in counter:
            if num != 0:
                return False
        return True
