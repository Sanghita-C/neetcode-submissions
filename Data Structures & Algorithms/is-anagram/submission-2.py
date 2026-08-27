class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Questions: 
         - length of string ? huge
         - can we have empty strings ? No
         - is it necessary both strings same len? No

        Algorithm : 

        Approach 1 Time O(n logn ) mem = o(1): 
        - check if len same:
            - No return False
        - sort both the strings
        - loop through both sorted string 
            - if char doesn't match
                    - return False
        - return True

        Approach 2 Time : O(n), mem = O(1): 
        - check if len same:
            - No return False
        - char_map_s1, char_map_s2 (26 char)
        - loop through each letter
            - increase the count in char_map
        - loop through both char_map:
            if count of char doesn't match 
                - return False
        - return True

        Test: 

        s = race, t= acer

        char_s = [a=1, c=1, e=1, r = 1, ], char_t = [a =1, c=1, e=1, r=1  ]

        s = ace, t= eat

        char_s = [a =1,c=1, e=1 ], char_t = [a=1, e=1, t=1 ]

        """

        if len(s) != len(t): 
            return False
        
        size = len(s)

        char_s = [0]*26
        char_t = [0]*26

        for i in range(size):
            char_s[ord(s[i])- ord('a')] +=1
            char_t[ord(t[i])- ord('a')] +=1

        for i in range(26):
            if char_s[i]!=char_t[i]:
                return False
        

        return True

        
        