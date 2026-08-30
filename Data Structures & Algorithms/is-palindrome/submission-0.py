class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Question: 
        - how long ? large enough 
        - trailing spaces? possible
        - case sensitivity ? No
        - Do we care about spaces ? -ignore all alpha bumeric part


        Algorithm :

        - convert the string into lowercase
        - start, end -initiate
        - while start <= end: 
            if s[start] is not alphanum:
                start ++
                continue
            if s[end] is not alphnum: 
                end -- 
                continue

            if s[end] != s[start] :
                return False



        """

        s = s.lower()
        start, end = [0, len(s) - 1]

        while start <= end: 
            if ord(s[start]) < 48 or (ord(s[start])> 57 and ord(s[start])<97) or (ord(s[start]) > 122):
                start +=1
                continue
            if ord(s[end]) < 48 or (ord(s[end])> 57 and ord(s[end])<97) or (ord(s[end]) > 122):
                end -=1
                continue
            
            if s[end] != s[start]:
                return False
            start+=1
            end -=1

        return True
        