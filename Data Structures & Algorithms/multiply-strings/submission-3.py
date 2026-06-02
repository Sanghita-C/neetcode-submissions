class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        size1 = len(num1)
        size2 = len(num2)

        carry = 0
        level = 0
        level_output = ""
        level_output_list = []
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(size1):
            for j in range(size2):
                digit1 = int(num1[i])
                digit2 = int(num2[j])

                prod = (digit1 * digit2) + carry

                carry = int(prod/10)
                level_output += str(prod%10)
                #print(level_output)
                #print(carry)

                if j== size2 -1:
                    level_output += str(carry)
                    level_output = level_output[:: -1]
                    #print(level_output)
                    trail_zero ="0"*level
                    level_output += trail_zero
                    level_output_list.append(level_output)
                    level +=1
                    carry = 0
                    level_output = ""

        sum = 0
        for num in level_output_list: 
            #print(num)
            #print(type(num))
            num = int(num)
            sum += num
        
        return str(sum)


        