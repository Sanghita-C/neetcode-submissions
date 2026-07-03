class Solution:
    def calculate(self, s: str) -> int:
        """
        --> remove the spaces 
        ---> DMAS
        first pass - division
        ...last pass - addition

        parsing the string : 

        "32 +16 -26/2 +6" 
        list = 32, +, 16, - , 26, /, 2, +, 6

        prev operand (PO)
        prev_ids (PI)
                                       po
        div _pass = 32 + 16 - 13 # # + 6

                            PO     i 
        add_pass  = 48 # # -19 # # # #

        for any calculation: 
            take the PO and PI
            do the operation
            change the value of PO
            make the next operand and operator as #
        """

        size = len(s)
        #print(s)
        operand = ""
        math_expression_list = []

        for character in s:
            if character != " " and character not in ["+", "-", "/", "*"]:
                operand += character
            elif character in ["+", "-", "/", "*"]:
                math_expression_list.append(int(operand))
                math_expression_list.append(character)
                operand = ""
        math_expression_list.append(int(operand))
        # div pass
        prev_operand = math_expression_list[0]
        prev_idx = 0
        n = len(math_expression_list)
        if n==1:
            return math_expression_list[0]

        print(f"math exp is {math_expression_list}")

        for i in range(1,n):
            if math_expression_list[i] not in ["+", "-", "/", "*", "#"]:
                prev_operand = math_expression_list[i]
                prev_idx = i
            elif math_expression_list[i] == "/"or math_expression_list[i] =="*":
                next_operand = math_expression_list[i+1]
                if math_expression_list[i] =="/":
                    result = int(prev_operand/next_operand)
                else:
                    result = prev_operand * next_operand
                
                prev_operand = result
                math_expression_list[prev_idx] = prev_operand
                #print(f"result of division is {result} and stored at idx {prev_idx}")
                math_expression_list[i+1] = "#"
                math_expression_list[i] = "#"

        #print(f"math exp after div is {math_expression_list}")

        #multiplication pass
        prev_operand = math_expression_list[0]
        prev_idx = 0

        for i in range(1,n):
            if math_expression_list[i] not in ["+", "-", "/", "*", "#"]:
                prev_operand = math_expression_list[i]
                prev_idx = i
            elif math_expression_list[i] == "*":
                #print(i)
                next_operand = math_expression_list[i+1]
                result = prev_operand * next_operand
                prev_operand = result
                math_expression_list[prev_idx] = prev_operand
                #print(f"result of multiplication is {result} and stored at idx {prev_idx}")
                math_expression_list[i+1] ="#"
                math_expression_list[i] = "#"
        
        #print(f"math exp after mul is {math_expression_list}")

        #add pass
        prev_operand = math_expression_list[0]
        prev_idx = 0

        for i in range(1,n):
            if math_expression_list[i] not in ["+", "-", "/", "*", "#"]:
                prev_operand = math_expression_list[i]
                prev_idx = i
            elif math_expression_list[i] == "+" or math_expression_list[i] =="-" :
                next_operand = math_expression_list[i+1]
                if math_expression_list[i] =="+":
                    result = prev_operand + next_operand
                else:
                    result = prev_operand - next_operand
                prev_operand = result
                math_expression_list[prev_idx] = prev_operand
                #print(f"result of add is {result} and stored at idx {prev_idx}")
                math_expression_list[i+1] = "#"
                math_expression_list[i] = "#"

        #print(f"math exp after add is {math_expression_list}")

        #sub pass
        prev_operand = math_expression_list[0]
        #print(f"debug prev_operand = {prev_operand}" )
        prev_idx = 0

        for i in range(1,n):
            if math_expression_list[i] not in ["+", "-", "/", "*", "#"]:
                prev_operand = math_expression_list[i]
                prev_idx = i
            elif math_expression_list[i] == "-":
                next_operand = math_expression_list[i+1]
                result = prev_operand - next_operand
                prev_operand = result
                math_expression_list[prev_idx] = prev_operand
                #print(f"result of sub is {result} and stored at idx {prev_idx}")
                math_expression_list[i+1] ="#"
                math_expression_list[i] = "#"

        #print(f"math exp after sub is {math_expression_list}")

        return math_expression_list[0]




        