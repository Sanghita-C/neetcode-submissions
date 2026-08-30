class Solution:
    def isValid(self, s: str) -> bool:
        """
        open - ( { [
        close ) } ]


        [ ( )][()])
        stack [ [ (  ]. close ]

        Failure point : 
        -  close symbol and the last open symbol doesn't match
        -  close symbol with stack empty
        - at the end if the stack is not empty 

        """

        stack = []
        character_map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for character in s :
            if character in ['(', '{', '[']:
                stack.append(character)
            
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != character_map[character]:
                    return False
                stack.pop()
            
        if len(stack) !=0 : 
            return False
        
        return True

        