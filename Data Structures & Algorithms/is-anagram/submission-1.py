class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_counter = [0]*26

        # Mapping the counter of  string s 
        for x in s:
            character_counter[ord(x) - ord('a')] += 1
        
        #Mapping the counter of string t 
        for x in t : 
            character_counter[ord(x) - ord('a')] -=1
            if character_counter[ord(x) - ord('a')] < 0 : 
                return False

        for i in range(26):
            if character_counter[i] > 0:
                return False 
        
        return True